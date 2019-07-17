# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('lgb_sigma_psimu', {
        'values': "np.log10(mc['lgb_sigma_psimu'])",
        'bandwidth': [0.12],
        'nbins': 100,
        'range': "[np.min(np.log10(mc['lgb_sigma_psimu']))-0.5, \
                   np.max(np.log10(mc['lgb_sigma_psimu']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': [0.148],
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

grid = None
