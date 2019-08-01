# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.25, 5), #[0.13]
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.05, 0.35, 7), #[0.30]
        'nbins': 400,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.05, 0.35, 7), #[0.30 ]
        'nbins': 100,
        'range': None
        })
])

grid = None
