# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('lgb_sigma_psimu', {
        'values': "np.log10(mc['lgb_sigma_psimu'])",
        'bandwidth': [0.06],
        'nbins': 100,
        'range': None
        }),
    ('psi_mu', {
        'values': "np.log10(mc['psi_mu'])",
        'bandwidth': [0.16],
        'nbins': 400,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': [0.12],
        'nbins': 100,
        'range': None
        })
])

grid = None