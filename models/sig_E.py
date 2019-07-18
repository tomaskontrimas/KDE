# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('lgb_sigma_psimu', {
        'values': "np.log10(mc['lgb_sigma_psimu'])",
        'bandwidth': np.linspace(0.2, 0.06, 5), #[0.04]
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.16, 0.20, 5), #[0.18]
        'nbins': 100,
        'range': None
        })
])

grid = None
