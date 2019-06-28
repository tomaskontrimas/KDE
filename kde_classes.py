# -*- coding: utf-8 -*-

import numpy as np
import os

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


class Model(object):
    """docstring for Model"""
    def __init__(self, mc, settings, index=None, weight=None, gamma=2.0, phi0=1):
        super(Model, self).__init__()
        self.settings = settings
        #self.values = []
        self.nbins = []
        self.bandwidths = []
        self.spaces = []
        self.approx_pdf = 0
        self.var_names = []
        self.tree = None
        self.kde_norm = 1.0
        self.mc = mc
        self.weights = None
        self.phi0 = phi0
        self.gamma = gamma

        if index is not None:
            mc = self.mc[index]
        self._initialize_model(mc)

    def _initialize_model(self, mc):
        for key in self.settings:
            # Generate lists of needed variables.
            self.var_names.append(key)
            self.nbins.append(self.settings[key]['nbins'])
            self.bandwidths.append(self.settings[key]['bandwidth'])

            # Calculate values.
            if callable(self.settings[key]['function']):
                #self.values.append(self.settings[key]['function'](mc[self.settings[key]['variable']]))
                value = self.settings[key]['function'](mc[self.settings[key]['variable']])
            else:
                #self.values.append(mc[self.settings[key]['variable']])
                value = mc[self.settings[key]['variable']]

            # Name or just the key?
            self.spaces.append(OneDimPhaseSpace(self.settings[key]['name'], *self.settings[key]['range']))

            if not self.tree:
                value_array = np.array(value, dtype=[(self.settings[key]['name'],
                                       np.float32)])
                self.tree = array2tree(value_array)
            else:
                value_array = np.array(value, dtype=[(self.settings[key]['name'],
                                       np.float32)])
                array2tree(value_array, tree=self.tree)

            # calculate normalization
            self.kde_norm /= self.settings[key]['range'][1] - self.settings[key]['range'][0]

        self._generate_weights(mc, weight)

        array2tree(np.array(self.weights, dtype=[("weight", np.float32)]),
                   tree=self.tree)

        self.space = CombinedPhaseSpace("PhspCombined", *self.spaces)


    def _generate_weights(self, mc, weight=None):
        # phi0 in units of 1e-18 1/GeV/cm^2/sr/s
        self.phi0 *= 1e-18
        if weight == 'pl':
            self.weights = mc['orig_OW']*powerlaw(
                mc['trueE'], phi0=self.phi0, gamma=self.gamma)
        elif weight == 'conv':
            self.weights = mc['conv']
        elif weight == 'conv+pl':
            diff_weight = mc['orig_OW']*powerlaw(
                mc['trueE'], phi0=self.phi0, gamma=self.gamma)
            self.weights = mc['conv'] + diff_weight
            # print('Rates [1/yr]:')
            # print(np.sum(self.mc['conv']) * np.pi * 1e7)
            # print(np.sum(diff_weight) * np.pi * 1e7)
        else:
            self.weights = np.ones(len(mc))
            print('Using ones as weight.')

    def update_model(self, mc, settings=None):
        if settings is not None:
            self.settings = settings
        self._initialize_model(mc)


class KDE(object):
    """docstring for KDE"""
    def __init__(self, model, adaptive=False):
        super(KDE, self).__init__()
        self.model = model
        self.binned_kernel = None
        self.adaptive_kernel = None

    def generate_binned_kernel_density(self):
        args = []
        args.extend([
            "BinnedKernelDensity",
            self.model.space,
            self.model.tree
        ])
        args.extend(self.model.var_names)
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
            self.model.space,
            self.model.tree
        ])
        args.extend(self.model.var_names)
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
