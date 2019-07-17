# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('lgb_sigma_psimu', {
        'values': "np.log10(mc['lgb_sigma_psimu'])",
        'bandwidth': [0.04],
        'nbins': 200,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': [0.18],
        'nbins': 200,
        'range': None
        })
])

grid = None
