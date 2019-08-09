# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = {}

settings['default'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.01, 0.30, 30), #[0.1]
        'nbins': 150,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.01, 0.40, 40), #[0.18]
        'nbins': 150,
        'range': None
        })
])

settings['2.0'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.01, 0.10, 30), #[0.1]
        'nbins': 150,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.01, 0.10, 40), #[0.18]
        'nbins': 150,
        'range': None
        })
])


grid = None
