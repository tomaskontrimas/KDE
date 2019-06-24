#!/usr/bin/env python

import numpy as np

def setup_KDE(mc_vals, cfg_keys=None):
    settings = {
        'logsigma': {
            'name': 'logsigma',
            'values': np.log(mc_vals['muex_sigma']),
            'bandwidth': 0.1,
            'nbins': 100,
            'range': [0.0, 1.0]
            },
        'sinDec': {
            'name': 'sinDec',
            'values': -np.cos(mc_vals['mu_zenith']),
            'bandwidth': 0.1,
            'nbins': 100,
            'range': [-1.0, 1.0]
            },

        'logEr': {
            'name': 'logEr',
            'values': mc_vals['loge_muex'],
            'bandwidth': 0.1,
            'nbins': 100,
            'range': [0.0, 1.0]
            }
    }

    #grid = np.linspace(0, 1, 1000)
    grid = None

    return settings, grid
