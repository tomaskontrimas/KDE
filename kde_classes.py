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
        self.tree = None
        self.kde_norm = 1.0


        for key in settings:
            # Generate lists of needed variables.
            self.var_names.append(key)
            self.nbins.append(settings[key]['nbins'])
            self.bandwidths.append(settings[key]['bandwidth'])

            # Calculate values.
            if callable(settings[key]['function']):
                #self.values.append(settings[key]['function'](mc[settings[key]['variable']]))
                value = settings[key]['function'](mc[settings[key]['variable']])
            else:
                #self.values.append(mc[settings[key]['variable']])
                value = mc[settings[key]['variable']]

            # Name or just the key?
            self.spaces.append(OneDimPhaseSpace(settings[key]['name'], *settings[key]['range']))

            if not self.tree:
                self.tree = array2tree(np.array(value, dtype=[(settings[key]['name'], np.float32)]))
            else:
                array2tree(np.array(value, dtype=[(settings[key]['name'], np.float32)]), tree=self.tree)

            # calculate normalization
            self.kde_norm /= settings[key]['range'][1] - settings[key]['range'][0]


        #array2tree(np.array(self.weights, dtype=[("weight", np.float32)]),
        #           tree=self.tree)

        self.space = CombinedPhaseSpace("PhspCombined", *self.spaces)


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
        #args.append("weight")
        args.extend(self.model.nbins)
        args.extend(self.model.bandwidths)
        args.extend([self.model.approx_pdf, 0])

        self.binned_kernel = BinnedKernelDensity(*args)

        return self.binned_kernel

    def generate_adaptive_kernel_density(self, pdf_seed=None):
        # Set or generate pdf_seed if not provided.
        if not pdf_seed:
            if not self.binned_kernel:
                self.generate_binned_kernel_density()
            else:
                pdf_seed = self.binned_kernel

        args = []
        args.extend([
            "AdaptiveKernelDensity",
            self.model.space,
            self.model.tree
        ])
        args.extend(self.model.var_names)
        #args.append("weight")
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
