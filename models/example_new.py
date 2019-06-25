# -*- coding: utf-8 -*-

import numpy as np

settings = {
    'logsigma': {
        'name': 'logsigma',
        'variable': 'muex_sigma',
        'function': np.log,
        'bandwidth': 0.1,
        'nbins': 100,
        'range': [0.0, 1.0]
        },
    'sinDec': {
        'name': 'sinDec',
        'variable': 'mu_zenith',
        'function': np.cos,
        'bandwidth': 0.1,
        'nbins': 100,
        'range': [-1.0, 1.0]
        },

    'logEr': {
        'name': 'logEr',
        'variable': 'loge_muex',
        'function': None,
        'bandwidth': 0.1,
        'nbins': 100,
        'range': [0.0, 1.0]
        }
}

#grid = np.linspace(0, 1, 1000)
grid = None
