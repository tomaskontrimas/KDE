# -*- coding: utf-8 -*-

import importlib
import itertools
import logging
import numpy as np
import os

from sklearn.model_selection import KFold
from scipy.interpolate import RegularGridInterpolator

from config import CFG
from dataset import load_and_prepare_data
from functions import (
    pl_weighting,
    conv_weighting,
    conv_pl_weighting,
    plotter_wkde_weighting
)

# ROOT imports.
os.environ["ROOT_INCLUDE_PATH"] = os.pathsep + CFG['paths']['meerkat_root']
from ROOT import gSystem, gStyle, RooRealVar, std, Double
gSystem.Load(CFG['paths']['meerkat_lib'])

from ROOT import (
    OneDimPhaseSpace,
    CombinedPhaseSpace,
    BinnedKernelDensity,
    AdaptiveKernelDensity,
    Logger
)

from root_numpy import array2tree

# Set Meerkat log level to Errors
Logger.setLogLevel(2)


class Model(object):
    """The Model class initializes and stores variables based on the provided
    model settings file. It is used for the KDE instance generation.
    """
    def __init__(self, model_module, mc=None, weighting=None, gamma=2.0,
                 phi0=1):
        super(Model, self).__init__()
        self.logger = logging.getLogger('KDE.' + __name__ + '.Model')
        model = importlib.import_module('models.{}'.format(model_module))
        settings = model.settings
        grid = model.grid

        if mc is None:
            if CFG['paths']['IC_mc'] is not None:
                mc = load_and_prepare_data(CFG['paths']['IC_mc'])
            else:
                raise ValueError('No suitable Monte Carlo provided.')

        self.values = [eval(settings[key]['values']) for key in settings]
        self.vars = [key for key in settings]
        self.bandwidth_vars = [key + '_bandwidth' for key in settings]
        self.nbins = [settings[key]['nbins'] for key in settings]
        self.bandwidths = [settings[key]['bandwidth'] for key in settings]
        self.ranges = [eval(str(settings[key]['range']))
                       if settings[key]['range'] is not None
                       else [min(self.values[i]), max(self.values[i])]
                       for i, key in enumerate(settings)]
        self.mc = mc
        self.phi0 = phi0*1e-18  # Renormalize in units of 1e-18 1/GeV/cm^2/sr/s.
        self.gamma = gamma

        # Calculate KDE normalization.
        range_norm = [1.0] + [bound[1] - bound[0] for bound in self.ranges]
        self.kde_norm = reduce((lambda x, y : x/y), range_norm)

        self.default_weighting_dict = {
            'pl': pl_weighting,
            'conv': conv_weighting,
            'conv+pl': conv_pl_weighting,
            'plotter_wkde': plotter_wkde_weighting
        }
        self.weights = self._generate_weights(weighting)

        if grid is None:
            self.out_bins = [np.linspace(self.ranges[i][0], self.ranges[i][1],
                                         self.model.nbins[i])
                             for i, key in enumerate(settings)]
        else:
            self.out_bins = [grid[key] for key in settings]
            if self.out_bins.shape != self.nbins:
                raise ValueError('Grid shape are not equal to defined nbins.')
        self.coords = np.array(list(itertools.product(*out_bins)))

    def _generate_weights(self, weighting):
        if callable(weighting):
            return weighting(self.mc, self.phi0, self.gamma)
        elif isinstance(weighting, list):
            if len(weighting) != len(self.mc):
                raise ValueError('Weighting list length should be equal to the '
                                 'MC length.')
            return weighting
        elif weighting in self.default_weighting_dict:
            return self.default_weighting_dict[weighting](self.mc, self.phi0,
                                                          self.gamma)
        else:
            self.logger.info('Using ones as weight.')
            return np.ones(len(self.mc))


class KDE(object):
    """docstring for KDE"""
    def __init__(self, model):
        super(KDE, self).__init__()
        self.logger = logging.getLogger('KDE.' + __name__ + '.KDE')
        self.model = model
        self.binned_kernel = None
        self.adaptive_kernel = None
        self.cv_result = np.array([], dtype={
            'names': self.model.bandwidth_vars + ['LLH', 'Zeros'],
            'formats': ['f4']*len(self.model.bandwidth_vars) + ['f4', 'f4']
        })
        self.cv_results = np.array(self.cv_result)

        self._generate_tree_and_space()

    def _generate_tree_and_space(self, index=None):
        self.tree = None
        spaces = []
        if index is None:
            index = slice(len(self.model.values[0])) # Index the whole array.
        for i, var in enumerate(self.model.vars):
            spaces.append(OneDimPhaseSpace(var, *self.model.ranges[i]))
            if self.tree is None:
                value_array = np.array(self.model.values[i][index], dtype=[(var, np.float32)])
                self.tree = array2tree(value_array)
            else:
                value_array = np.array(self.model.values[i][index], dtype=[(var, np.float32)])
                array2tree(value_array, tree=self.tree)

        array2tree(np.array(self.model.weights[index],
            dtype=[("weight", np.float32)]), tree=self.tree)

        self.space = CombinedPhaseSpace("PhspCombined", *spaces)

    def generate_binned_kd(self, bandwidth):
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
        args.extend([0, 0])

        self.binned_kernel = BinnedKernelDensity(*args)

        return self.binned_kernel

    def generate_adaptive_kd(self, bandwidth, pdf_seed=None):
        # Set or generate pdf_seed if not provided.
        if pdf_seed is None:
            pdf_seed = self.generate_binned_kd(bandwidth)

        args = []
        args.extend([
            "AdaptiveKernelDensity",
            self.space,
            self.tree
        ])
        args.extend(self.model.vars)
        args.append("weight")
        args.extend(self.model.nbins)
        args.extend(bandwidth)
        args.extend([pdf_seed,
                     pdf_seed,
                     0])

        self.adaptive_kernel = AdaptiveKernelDensity(*args)

        return self.adaptive_kernel

    def eval_point(self, kernel_density, coord):
        l = len(coord)
        v = std.vector(Double)(l)
        for i in range(l):
            v[i] = coord[i]
        return kernel_density.density(v)*self.model.kde_norm

    def cross_validate(self, bandwidth, adaptive=False, pdf_seed=None):
        kfold = KFold(n_splits=CFG['project']['n_splits'],
                      random_state=CFG['project']['random_state'], shuffle=True)
        llh = []
        zeros = []
        for training_index, validation_index in kfold.split(self.model.mc):
            self._generate_tree_and_space(training_index)

            if adaptive:
                kernel_density = self.generate_adaptive_kd(bandwidth, pdf_seed)
            else:
                kernel_density = self.generate_binned_kd(bandwidth)

            training_pdf_vals = self.get_pdf_values(kernel_density)

            # Validation
            rgi_pdf = RegularGridInterpolator(tuple(out_bins), training_pdf_vals,
                method='linear', bounds_error=False, fill_value=0)

            mc_validation_values = []
            for i, var in enumerate(self.model.vars):
                mc_validation_values.append(
                    self.model.values[i][validation_index])

            likelihood = rgi_pdf(zip(*mc_validation_values))
            inds = likelihood > 0.

            weights = self.model.weights[validation_index]
            weights /= np.sum(weights)

            llh.append(np.sum(np.log(likelihood[inds])*weights[inds]))
            zeros.append(len(likelihood) - len(inds))
        result_tuple = tuple(list(bandwidth)
                             + [np.average(llh), np.average(zeros)])
        self.cv_result = np.array([result_tuple], dtype=self.cv_result.dtype)
        return self.cv_result

    def cross_validate_bandwidths(self, bandwidths=None, adaptive=False,
                                  pdf_seed=None):
        if bandwidths is None:
            bandwidths = self.model.bandwidths
        for bandwidth in itertools.product(*bandwidths):
            self.logger.info('Bandwidth: %s', bandwidth)
            result = self.cross_validate(bandwidth, adaptive)
            self.cv_results = np.append(self.cv_results, result)
        return self.cv_results

    def get_pdf_values(self, kernel_density):
        pdf_values = np.asarray([self.eval_point(kernel_density, coord)
                               for coord in self.model.coords])
        pdf_values = pdf_values.reshape(self.model.nbins)
        return pdf_values
