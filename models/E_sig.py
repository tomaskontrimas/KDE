# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': [0.08],
        'nbins': 200,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': [0.15],
        'nbins': 200,
        'range': None
        })
])

grid = None
