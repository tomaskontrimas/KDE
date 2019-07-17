# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.06, 0.10, 5), #[0.08]
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.02, 0.6, 5), #[0.04]
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.15, 0.19, 5), #[0.17]
        'nbins': 100,
        'range': None
        })
])

grid = None
