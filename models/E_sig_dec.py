# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': [0.05],
        'nbins': 100,
        'range': None
        }),
    ('trueDec', {
        'values': "np.sin(mc['trueDec'])",
        'bandwidth': [0.15],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('logE', {
        'values': "mc['logE']",
        'bandwidth': [0.18],
        'nbins': 100,
        'range': None
        })
])

grid = None
