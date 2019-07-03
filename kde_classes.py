# -*- coding: utf-8 -*-

import numpy as np
import os
import itertools


from config import CFG
from functions import powerlaw

os.environ["ROOT_INCLUDE_PATH"] = os.pathsep + CFG['paths']['meerkat_root']
from ROOT import gSystem, gStyle, RooRealVar, std, Double
gSystem.Load(CFG['paths']['meerkat_lib'])

from ROOT import (
    OneDimPhaseSpace,
    CombinedPhaseSpace,
    BinnedKernelDensity,
    AdaptiveKernelDensity
)

from root_numpy import array2tree

from sklearn.model_selection import KFold
from scipy.interpolate import RegularGridInterpolator

class Model(object):
    """docstring for Model"""
    def __init__(self, mc, settings, index=None, weight=None, gamma=2.0, phi0=1):
        super(Model, self).__init__()
        # self.settings = settings
        #self.values = []
        self.vars = [key for key in settings]
        self.mc_vars = [settings[key]['mc_var'] for key in settings]
        self.nbins = [settings[key]['nbins'] for key in settings]
        self.bandwidths = [settings[key]['bandwidth'] for key in settings]
        self.functions = [settings[key]['function'] for key in settings]
        self.ranges = [settings[key]['range'] for key in settings]
        self.mc = mc
        self.weights = None
        # phi0 in units of 1e-18 1/GeV/cm^2/sr/s
        self.phi0 = phi0*1e-18
        self.gamma = gamma
        self.approx_pdf = 0

        # calculate normalization
        range_norm = [1.0] + [settings[key]['range'][1]
                              - settings[key]['range'][0] for key in settings]
        self.kde_norm = reduce((lambda x, y : x/y), range_norm)


class KDE(object):
    """docstring for KDE"""
    def __init__(self, model, index=None, adaptive=False):
        super(KDE, self).__init__()
        self.model = model
        self.binned_kernel = None
        self.adaptive_kernel = None

        #self.weights = None

        self.tree = None
        self.spaces = []

        if index is not None:
            mc = self.model.mc[index]
        else:
            mc = self.model.mc

        self._generate_tree_and_space(mc)

    def _generate_tree_and_space(self, mc):
        for i, var in enumerate(self.model.vars):
            # Calculate values.
            if callable(self.model.functions[i]):
                mc_values = self.model.functions[i](mc[self.model.mc_vars[i]])
            else:
                mc_values = mc[self.model.mc_vars[i]]

            # Name or just the key?
            self.spaces.append(OneDimPhaseSpace(var, *self.model.ranges[i]))

            if self.tree is None:
                value_array = np.array(mc_values, dtype=[(var, np.float32)])
                self.tree = array2tree(value_array)
            else:
                value_array = np.array(mc_values, dtype=[(var, np.float32)])
                array2tree(value_array, tree=self.tree)

        weights = self._generate_weights(mc)

        array2tree(np.array(weights, dtype=[("weight", np.float32)]),
                   tree=self.tree)

        self.space = CombinedPhaseSpace("PhspCombined", *self.spaces)

    def _generate_weights(self, mc, weight_type=None):
        if weight_type == 'pl':
            weights = mc['orig_OW']*powerlaw(
                mc['trueE'], phi0=self.model.phi0, gamma=self.model.gamma)
        elif weight_type == 'conv':
            weights = mc['conv']
        elif weight_type == 'conv+pl':
            diff_weight = mc['orig_OW']*powerlaw(
                mc['trueE'], phi0=self.model.phi0, gamma=self.model.gamma)
            weights = mc['conv'] + diff_weight
            # print('Rates [1/yr]:')
            # print(np.sum(self.mc['conv']) * np.pi * 1e7)
            # print(np.sum(diff_weight) * np.pi * 1e7)
        else:
            weights = np.ones(len(mc))
            print('Using ones as weight.')
        return weights

    def generate_binned_kernel_density(self):
        args = []
        args.extend([
            "BinnedKernelDensity",
            self.space,
            self.tree
        ])
        args.extend(self.model.vars)
        args.append("weight")
        args.extend(self.model.nbins)
        args.extend(self.model.bandwidths)
        args.extend([self.model.approx_pdf, 0])

        self.binned_kernel = BinnedKernelDensity(*args)

        return self.binned_kernel

    def generate_adaptive_kernel_density(self, pdf_seed=None):
        # Set or generate pdf_seed if not provided.
        if not pdf_seed:
            if self.binned_kernel:
                pdf_seed = self.binned_kernel
            else:
                pdf_seed = self.generate_binned_kernel_density()

        args = []
        args.extend([
            "AdaptiveKernelDensity",
            self.space,
            self.tree
        ])
        args.extend(self.model.vars)
        args.append("weight")
        args.extend(self.model.nbins)
        args.extend(self.model.bandwidths)
        args.extend([pdf_seed,
                     self.model.approx_pdf,
                     0])

        self.adaptive_kernel = AdaptiveKernelDensity(*args)

        return self.adaptive_kernel

    #@staticmethod
    def eval_point(self, point):
        l = len(point)
        v = std.vector(Double)(l)
        for i in range(l):
            v[i] = point[i]
        if self.adaptive_kernel:
            return self.adaptive_kernel.density(v)*self.model.kde_norm
        elif self.binned_kernel:
            return self.binned_kernel.density(v)*self.model.kde_norm
        else:
            print('No kernel found.')

    def cross_validate(self):
        kfold = KFold(n_splits=5, random_state=0, shuffle=True)

        for training_index, validation_index in kfold.split(self.model.mc):
            print("training_index", training_index)
            print("validation_index", validation_index)

            self.tree = None
            self.spaces = []
            self._generate_tree_and_space(self.model.mc[training_index])
            binned_kernel_density = self.generate_binned_kernel_density()


            out_bins = []
            for i, key in enumerate(self.model.vars):
                out_bins.append(np.linspace(self.model.ranges[i][0],
                                        self.model.ranges[i][1],
                                        self.model.nbins[i]))
            coords = np.array(list(itertools.product(*out_bins)))
            training_pdf_vals = np.asarray([self.eval_point(coord) for coord in coords])

            print("Coords: ", coords)
            print("training_pdf_vals: ", training_pdf_vals)

            rgi_pdf = RegularGridInterpolator(tuple(out_bins), training_pdf_vals)

    # #         shape = np.ones(len(self.model.vars), dtype=int)*nbins
    # #         adaptive_pdf_vals = adaptive_pdf_vals.reshape(*shape)

    # def cross_validate(self):
    #     kfold = KFold(n_splits=5, random_state=0, shuffle=True)
    #     lh_arr, zero_arr = [], []

    #     out_bins = []
    #     for i, key in enumerate(self.model.vars):
    #         out_bins.append(np.linspace(self.model.ranges[i][0],
    #                                 self.model.ranges[i][1],
    #                                 self.model.nbins[i]))
    #     coords = np.array(list(itertools.product(*out_bins)))

    #     for training_index, validation_index in kfold.split(self.model.mc):
    #         print('loop')
    #         #kde = KDE(self.model, index=training_index, adaptive=False)
    #         self._generate_tree_and_space(self.model.mc[training_index])
    #         binned_kernel_density = self.generate_binned_kernel_density()
    #         nbins = 100
    #         adaptive_pdf_vals = np.asarray([self.eval_point(coord) for coord in coords])
    # #         shape = np.ones(len(self.model.vars), dtype=int)*nbins
    # #         adaptive_pdf_vals = adaptive_pdf_vals.reshape(*shape)

    #         mc_validation = self.model.mc[validation_index]
    #         mc_validation_values = []

    #         # Calculate values.
    #         for i, var in enumerate(self.model.vars):
    #             if callable(self.model.functions[i]):
    #                 mc_validation_values.append(self.model.functions[i](mc_validation[var]))
    #             else:
    #                 mc_validation_values.append(mc_validation[var])

    #         mc_validation_values = np.array(list(itertools.product(*mc_validation_values)))
    #         print(mc_validation_values)

    #         coords = itertools.product(*out_bins)
    #         print("Coords: ", coords)
    #         #lh, zeros = do_validation(coords, adaptive_pdf_vals, mc_validation_values)
    #         lh, zeros = self.do_validation(out_bins, adaptive_pdf_vals, mc_validation_values)
    #         print('Number of zeros {}'.format(zeros))
    #         print('Likelihood Value {}'.format(lh))
    #         zero_arr.append(zeros)
    #         lh_arr.append(lh)
    #     fname = ''
    #     for i in range(len(args['bw'])):
    #         fname += '{}_{}_'.format(args['bw_key'][i], args['bw'][i])
    #     fname = fname[:-1] + '.npy'
    #     odict = {'zeros': zero_arr, 'lh': lh_arr}

    # def do_validation(self, coords, adaptive_pdf_vals, mc_validation_values):
    #     #old code:
    #     print("test:")
    #     print(coords)
    #     print(adaptive_pdf_vals)
    #     rgi_pdf = RegularGridInterpolator(coords, adaptive_pdf_vals,
    #                                   method='linear',
    #                                   bounds_error=False, fill_value=0)
    #     #weights = weights / np.sum(weights)
    #     likelihood = rgi_pdf(mc_validation_values)
    #     inds = likelihood > 0.
    #     #return np.sum(np.log(likelihood[inds]) * weights[inds]), len(likelihood) - len(inds)
    #     return np.sum(np.log(likelihood[inds])), len(likelihood) - len(inds)
