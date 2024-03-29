# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = {}

settings['default'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.13, 7),
        'bandwidth_adaptive': np.linspace(0.01, 0.13, 7),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': np.linspace(0.01, 0.13, 7),
        'bandwidth_adaptive': np.linspace(0.01, 0.13, 7),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['1.50'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.10, 0.20, 11),
        'bandwidth_adaptive': np.linspace(0.10, 0.20, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': [0.02],
        'bandwidth_adaptive': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['2.00'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.10, 0.30, 21),
        'bandwidth_adaptive': np.linspace(0.10, 0.30, 21),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': np.linspace(0.01, 0.025, 15),
        'bandwidth_adaptive': np.linspace(0.01, 0.025, 15),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.15, 0.35, 21),
        'bandwidth_adaptive': np.linspace(0.15, 0.35, 21),
        'nbins': 100,
        'range': None
        })
])

settings['2.10'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.25, 11),
        'bandwidth_adaptive': np.linspace(0.15, 0.25, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': [0.02],
        'bandwidth_adaptive': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['2.20'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.25, 11),
        'bandwidth_adaptive': np.linspace(0.15, 0.25, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': [0.02],
        'bandwidth_adaptive': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['2.30'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.25, 11),
        'bandwidth_adaptive': np.linspace(0.15, 0.25, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': [0.02],
        'bandwidth_adaptive': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['2.40'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.25, 11),
        'bandwidth_adaptive': np.linspace(0.15, 0.25, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': [0.02],
        'bandwidth_adaptive': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['2.50'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.25, 11),
        'bandwidth_adaptive': np.linspace(0.15, 0.25, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': [0.02],
        'bandwidth_adaptive': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['2.60'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.25, 11),
        'bandwidth_adaptive': np.linspace(0.15, 0.25, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': [0.02],
        'bandwidth_adaptive': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['2.70'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.25, 11),
        'bandwidth_adaptive': np.linspace(0.15, 0.25, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': [0.02],
        'bandwidth_adaptive': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['2.80'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.25, 11),
        'bandwidth_adaptive': np.linspace(0.15, 0.25, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': [0.02],
        'bandwidth_adaptive': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['2.90'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.25, 11),
        'bandwidth_adaptive': np.linspace(0.15, 0.25, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': [0.02],
        'bandwidth_adaptive': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['3.00'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.25, 11),
        'bandwidth_adaptive': np.linspace(0.15, 0.25, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': [0.02],
        'bandwidth_adaptive': [0.02],
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 11),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 11),
        'nbins': 100,
        'range': None
        })
])

settings['3.50'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.11, 11),
        'bandwidth_adaptive': np.linspace(0.01, 0.11, 11),
        'nbins': 100,
        'range': None
        }),
    ('dec', {
        'values': "np.sin(mc['dec'])",
        'bandwidth_binned': np.linspace(0.005, 0.03, 6),
        'bandwidth_adaptive': np.linspace(0.005, 0.03, 6),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.06, 0.16, 11),
        'bandwidth_adaptive': np.linspace(0.06, 0.16, 11),
        'nbins': 100,
        'range': None
        })
])

grid = None
