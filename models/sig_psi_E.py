# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': [0.15], #[0.15]
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.42, 0.62, 11), #[0.20]
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': [0.56], #[0.35]
        'nbins': 150,
        'range': None
        })
])

grid = None
