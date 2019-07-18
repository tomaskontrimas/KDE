# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('lgb_sigma_psimu', {
        'values': "np.log10(mc['lgb_sigma_psimu'])",
        'bandwidth': np.linspace(0.04, 0.08, 5), #[0.06]
        'nbins': 100,
        'range': None
        }),
    ('psi_mu', {
        'values': "np.log10(mc['psi_mu'])",
        'bandwidth': np.linspace(0.14, 0.18, 5), #[0.16]
        'nbins': 400,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.10, 0.14, 5), #[0.12]
        'nbins': 100,
        'range': None
        })
])

grid = None
