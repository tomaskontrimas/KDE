# -*- coding: utf-8 -*-

import numpy as np
import os

from config import CFG

os.environ["ROOT_INCLUDE_PATH"] = os.pathsep + CFG['paths']['meerkat_root_path']
from ROOT import gSystem, gStyle, RooRealVar, std, Double
gSystem.Load(CFG['paths']['meerkat_path'])

from ROOT import (
    OneDimPhaseSpace,
    CombinedPhaseSpace,
    BinnedKernelDensity,
    AdaptiveKernelDensity
)

from root_numpy import array2tree


class Model(object):
    """docstring for Model"""
    def __init__(self, mc, settings):
        super(Model, self).__init__()
        #self.settings = settings
        #self.values = []
        self.nbins = []
        self.bandwidths = []
        self.spaces = []
        self.approx_pdf = 0
        self.var_names = []
        self.tree = array2tree(np.array([]))
        self.kde_norm = 1.0


        for key in settings:
            # Generate lists of needed variables.
            self.var_names.append(key)
            self.nbins.append(key['nbins'])
            self.bandwidths.append(key['bandwidth'])

            # Calculate values.
            if callable(key['function']):
                #self.values.append(key['function'](mc[key['variable']]))
                value = key['function'](mc[key['variable']])
            else:
                #self.values.append(mc[key['variable']])
                value = mc[key['variable']]

            # Name or just the key?
            self.spaces.append(OneDimPhaseSpace(key['name'], *key['range']))

            array2tree(np.array(value, dtype=[(key['name']), np.float32]),
                       tree=self.tree)

            # calculate normalization
            self.kde_norm /= key['range'][1] - key['range'][0]

        #array2tree(np.array(self.weights, dtype=[("weight", np.float32)]),
        #           tree=self.tree)

        self.space = CombinedPhaseSpace(
                "PhspCombined", self.spaces[0], self.spaces[1])


class KDE(object):
    """docstring for KDE"""
    def __init__(self, model, adaptive=False):
        super(KDE, self).__init__()
        self.model = model
        self.binned_kernel = None




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

        self.binned_kernel = BinnedKernelDensity(args)

        # self.binned_kernel = BinnedKernelDensity(
        #     "BinnedKernelDensity",
        #     self.model.space,  # Phase space
        #     self.model.tree,  # Input ntuple
        #     *self.model.var_names,  # Variables to use
        #     "weight",      # weights
        #     *self.model.nbins,  # Numbers of bins
        #     *self.model.bandwidths,  # Kernel widths
        #     self.model.approx_pdf,  # Approximation PDF (0 for flat approximation)
        #     0)  # Sample size for MC convolution (0 for binned convolution)

        return self.binned_kernel

    # def generate_adaptive_kernel_density(self, pdf_seed=None):
    #     # Set or generate pdf_seed if not provided.
    #     if not pdf_seed:
    #         if not self.binned_kernel:
    #             self.generate_binned_kernel_density()
    #         else:
    #             pdf_seed = self.binned_kernel

    #     self.adaptive_kernel = AdaptiveKernelDensity(
    #         "AdaptiveKernelDensity",
    #         self.model.space,  # Phase space
    #         self.model.tree,  # Input ntuple
    #         *self.model.var_names,  # Variables to use
    #         "weight",      # weights
    #         *self.model.nbins,  # Numbers of bins
    #         *self.model.bandwidths,  # Kernel widths
    #         pdf_seed,  # PDF for width scaling
    #         0,  # Approximation PDF (0 for flat approximation)
    #         0)  # Sample size for MC convolution (0 for binned convolution)

    #     return self.adaptive_kernel

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
