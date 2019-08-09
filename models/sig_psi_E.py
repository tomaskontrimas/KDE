# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.concatenate((np.linspace(0.11, 0.13, 2),
                                     np.linspace(0.17, 0.19, 2))),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.concatenate((np.linspace(0.40, 0.42, 2),
                                     np.linspace(0.46, 0.48, 2))),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.52, 0.54, 2),
                                     np.linspace(0.58, 0.60, 2))),
        'nbins': 150,
        'range': None
        })
])

grid = None
