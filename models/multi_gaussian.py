# -*- coding: utf-8 -*-

import numpy as np

settings = {
    'x': {
        'mc_var': 'x',
        'function': None,
        'bandwidth': 0.5,
        'nbins': 100,
        'range': [-5, 5]
        },
    'y': {
        'mc_var': 'y',
        'function': None,
        'bandwidth': 0.5,
        'nbins': 100,
        'range': [-5, 5]
        }
}

#grid = np.linspace(0, 1, 1000)
grid = None
