# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = {}

settings['default'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.concatenate((np.linspace(0.11, 0.13, 2),
                                     np.linspace(0.17, 0.19, 2))),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.13, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.52, 0.54, 2),
                                     np.linspace(0.58, 0.60, 2))),
        'nbins': 100,
        'range': None
        })
])

settings['1.5'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.10, 0.40, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.13, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.65, 0.95, 7),
        'nbins': 100,
        'range': None
        })
])

settings['2.0'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.45, 0.75, 7),
        'nbins': 100,
        'range': None
        })
])

settings['2.1'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.45, 0.75, 7),
        'nbins': 100,
        'range': None
        })
])

settings['2.2'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.35, 0.65, 7),
        'nbins': 100,
        'range': None
        })
])

settings['2.3'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.35, 0.65, 7),
        'nbins': 100,
        'range': None
        })
])

settings['2.4'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.35, 0.65, 7),
        'nbins': 100,
        'range': None
        })
])

settings['2.5'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.35, 0.65, 7),
        'nbins': 100,
        'range': None
        })
])

settings['2.6'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.25, 0.55, 7),
        'nbins': 100,
        'range': None
        })
])

settings['2.7'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.25, 0.55, 7),
        'nbins': 100,
        'range': None
        })
])

settings['2.8'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.25, 0.55, 7),
        'nbins': 100,
        'range': None
        })
])

settings['2.9'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.15, 0.45, 7),
        'nbins': 100,
        'range': None
        })
])

settings['3.0'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.15, 0.45, 7),
        'nbins': 100,
        'range': None
        })
])

settings['3.5'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.35, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth': np.linspace(0.01, 0.07, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.10, 0.40, 7),
        'nbins': 100,
        'range': None
        })
])

grid = None
