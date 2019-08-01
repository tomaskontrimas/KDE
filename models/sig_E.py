# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('sigma', {
        'values': "np.log10(mc['sigma'])",
        'bandwidth': np.linspace(0.01, 0.20, 20), #[0.1]
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.10, 0.30, 21), #[0.17]
        'nbins': 100,
        'range': None
        })
])

grid = None
