# -*- coding: utf-8 -*-

import itertools
import logging
import numpy as np
from numpy.lib import recfunctions as np_rfn
import os

from sklearn.model_selection import KFold
from scipy.interpolate import RegularGridInterpolator

from config import CFG
from functions import powerlaw

# ROOT imports
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


class Model(object):
    """The Model class initializes and stores variables based on the provided
    model settings file. They are used for KDE instance generation.
    """
    def __init__(self, mc, settings, index=None, weighting=None, gamma=2.0,
                 phi0=1):
        super(Model, self).__init__()
        self.values = [eval(settings[key]['values']) for key in settings]
        self.vars = [key for key in settings]
        self.bandwidth_vars = [key + '_bandwidth' for key in settings]
        self.nbins = [settings[key]['nbins'] for key in settings]
        self.bandwidths = [settings[key]['bandwidth'] for key in settings]
        self.ranges = [settings[key]['range'] for key in settings]
        self.mc = mc
        self.weights = _generate_weights(weighting)
        self.phi0 = phi0*1e-18  # Renormalize in units of 1e-18 1/GeV/cm^2/sr/s.
        self.gamma = gamma
        self.approx_pdf = 0

        # Calculate KDE normalization.
        range_norm = [1.0] + [bound[1] - bound[0] for bound in self.ranges]
        self.kde_norm = reduce((lambda x, y : x/y), range_norm)
        self.logger = logging.getLogger(__name__ + 'Model')

    def _generate_weights(self, weighting):
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
            self.logger.info('Using ones as weight.')
        return weights


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

        self.results = np.array([], dtype={
            'names': self.bandwidth_vars + ['LLH', 'Zeros'],
            'formats': ['f4', 'f4', 'f4', 'f4']
        })

        if index is not None:
            mc = self.model.mc[index]
        else:
            mc = self.model.mc

        self._generate_tree_and_space(index)

    def _generate_tree_and_space(self, index):
        for i, var in enumerate(self.model.vars):
            # Calculate values.
            # if callable(self.model.functions[i]):
            #     mc_values = self.model.functions[i](mc[self.model.mc_vars[i]])
            # else:
            #     mc_values = mc[self.model.mc_vars[i]]
            #mc_values = eval(self.model.values[i])


            # Name or just the key?
            self.spaces.append(OneDimPhaseSpace(var, *self.model.ranges[i]))

            if self.tree is None:
                value_array = np.array(self.model.values[i][index], dtype=[(var, np.float32)])
                self.tree = array2tree(value_array)
            else:
                value_array = np.array(self.model.values[i][index], dtype=[(var, np.float32)])
                array2tree(value_array, tree=self.tree)

        array2tree(np.array(self.model.weights[index], dtype=[("weight", np.float32)]),
                   tree=self.tree)

        self.space = CombinedPhaseSpace("PhspCombined", *self.spaces)


    def generate_binned_kernel_density(self, bandwidth):
        args = []
        args.extend([
            "BinnedKernelDensity",
            self.space,
            self.tree
        ])
        args.extend(self.model.vars)
        args.append("weight")
        args.extend(self.model.nbins)
        args.extend(bandwidth)
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

    def cross_validate(self, bandwidth):
        kfold = KFold(n_splits=5, random_state=0, shuffle=True)
        llh = []
        zeros = []
        for training_index, validation_index in kfold.split(self.model.mc):
            self.tree = None
            self.spaces = []
            self._generate_tree_and_space(self.model.mc[training_index])
            binned_kernel_density = self.generate_binned_kernel_density(bandwidth)

            out_bins = []
            for i, key in enumerate(self.model.vars):
                out_bins.append(np.linspace(self.model.ranges[i][0],
                                        self.model.ranges[i][1],
                                        self.model.nbins[i]))
            coords = np.array(list(itertools.product(*out_bins)))
            training_pdf_vals = np.asarray([self.eval_point(coord) for coord in coords])
            nbins = 100
            shape = np.ones(len(self.model.vars), dtype=int)*nbins
            training_pdf_vals = training_pdf_vals.reshape(*shape)

            # Validation
            rgi_pdf = RegularGridInterpolator(tuple(out_bins), training_pdf_vals, method='linear', bounds_error=False, fill_value=0)

            mc = self.model.mc[validation_index]
            mc_validation_values = []

            # Calculate values.
            for i, var in enumerate(self.model.vars):
            #     if callable(self.model.functions[i]):
            #         mc_validation_values.append(self.model.functions[i](mc_validation[var]))
            #     else:
            #         mc_validation_values.append(mc_validation[var])
                mc_validation_values.append(eval(self.model.values[i]))

            likelihood = rgi_pdf(zip(*mc_validation_values))
            inds = likelihood > 0.

            llh.append(np.sum(np.log(likelihood[inds])))
            zeros.append(len(likelihood) - len(inds))
        #print("llh, zeros:", llh, zeros)
        return np.average(llh), np.average(zeros)

    def cross_validate_bandwidths(self):

        #print(self.model.bandwidths)
        result = np.array([['bandwidth', 0, 0]])

        for bandwidth in itertools.product(*self.model.bandwidths):
            print(bandwidth)
            llh, zeros = self.cross_validate(bandwidth)
            #result = np.append(result, [[str(bandwidth), llh, zeros]], axis=0)

            result_tuple = tuple(list(bandwidth) + [llh, zeros])
            result = np.array([result_tuple],
                              dtype=self.model.results.dtype)
            self.model.results = np.append(self.model.results, result)
        return self.model.results
