# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('lgb_sigma_psimu', {
        'values': "np.log10(mc['lgb_sigma_psimu'])",
        'bandwidth': np.linspace(0.01, 0.11, 11), #[0.04]
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.5, 0.25, 11), #[0.18]
        'nbins': 100,
        'range': None
        })
])

grid = None
