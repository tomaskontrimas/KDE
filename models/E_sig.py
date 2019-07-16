# -*- coding: utf-8 -*-

import numpy as np

settings = {
    'logSigma': {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': [0.08],
        'nbins': 200,
        'range': None
        },
    'logEr': {
        'values': "mc['logE']",
        'bandwidth': [0.15, 0.20],
        'nbins': 100,
        'range': None
        }
}

grid = None
