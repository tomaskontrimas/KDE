# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.05, 0.45, 20),
        'nbins': 400,
        'range': [np.sin(np.radians(-5)), 1.0]
        })
])

grid = None
