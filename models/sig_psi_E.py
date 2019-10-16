# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = {}

settings['default'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.14, 0.18, 5),
        'bandwidth_adaptive': np.linspace(0.14, 0.18, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.35, 0.39, 5),
        'bandwidth_adaptive': np.linspace(0.35, 0.39, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.77, 0.81, 5),
        'bandwidth_adaptive': np.linspace(0.77, 0.81, 5),
        'nbins': 100,
        'range': None
        })
])

settings['1.5'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.14, 0.18, 5),
        'bandwidth_adaptive': np.linspace(0.14, 0.18, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.35, 0.39, 5),
        'bandwidth_adaptive': np.linspace(0.35, 0.39, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.77, 0.81, 5),
        'bandwidth_adaptive': np.linspace(0.77, 0.81, 5),
        'nbins': 100,
        'range': None
        })
])

settings['2.0'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.14, 0.18, 5),
        'bandwidth_adaptive': np.linspace(0.14, 0.18, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.23, 0.27, 5),
        'bandwidth_adaptive': np.linspace(0.23, 0.27, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.38, 0.42, 5),
        'bandwidth_adaptive': np.linspace(0.38, 0.42, 5),
        'nbins': 100,
        'range': None
        })
])

settings['2.1'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.12, 0.16, 5),
        'bandwidth_adaptive': np.linspace(0.12, 0.16, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.21, 0.25, 5),
        'bandwidth_adaptive': np.linspace(0.21, 0.25, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.38, 0.42, 5),
        'bandwidth_adaptive': np.linspace(0.38, 0.42, 5),
        'nbins': 100,
        'range': None
        })
])

settings['2.2'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.13, 0.17, 5),
        'bandwidth_adaptive': np.linspace(0.13, 0.17, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.21, 0.25, 5),
        'bandwidth_adaptive': np.linspace(0.21, 0.25, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.38, 0.42, 5),
        'bandwidth_adaptive': np.linspace(0.38, 0.42, 5),
        'nbins': 100,
        'range': None
        })
])

settings['2.3'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.12, 0.16, 5),
        'bandwidth_adaptive': np.linspace(0.12, 0.16, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.21, 0.25, 5),
        'bandwidth_adaptive': np.linspace(0.21, 0.25, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.30, 0.34, 5),
        'bandwidth_adaptive': np.linspace(0.30, 0.34, 5),
        'nbins': 100,
        'range': None
        })
])

settings['2.4'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.12, 0.16, 5),
        'bandwidth_adaptive': np.linspace(0.12, 0.16, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.21, 0.25, 5),
        'bandwidth_adaptive': np.linspace(0.21, 0.25, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.35, 0.39, 5),
        'bandwidth_adaptive': np.linspace(0.35, 0.39, 5),
        'nbins': 100,
        'range': None
        })
])

settings['2.5'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.13, 0.17, 5),
        'bandwidth_adaptive': np.linspace(0.13, 0.17, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.19, 0.23, 5),
        'bandwidth_adaptive': np.linspace(0.19, 0.23, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.27, 0.31, 5),
        'bandwidth_adaptive': np.linspace(0.27, 0.31, 5),
        'nbins': 100,
        'range': None
        })
])

settings['2.6'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.13, 0.17, 5),
        'bandwidth_adaptive': np.linspace(0.13, 0.17, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.19, 0.23, 5),
        'bandwidth_adaptive': np.linspace(0.19, 0.23, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.25, 0.29, 5),
        'bandwidth_adaptive': np.linspace(0.25, 0.29, 5),
        'nbins': 100,
        'range': None
        })
])

settings['2.7'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.12, 0.16, 5),
        'bandwidth_adaptive': np.linspace(0.12, 0.16, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.13, 0.17, 5),
        'bandwidth_adaptive': np.linspace(0.13, 0.17, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.30, 0.34, 5),
        'bandwidth_adaptive': np.linspace(0.30, 0.34, 5),
        'nbins': 100,
        'range': None
        })
])

settings['2.8'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.14, 0.18, 5),
        'bandwidth_adaptive': np.linspace(0.14, 0.18, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.18, 0.22, 5),
        'bandwidth_adaptive': np.linspace(0.18, 0.22, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.16, 0.20, 5),
        'bandwidth_adaptive': np.linspace(0.16, 0.20, 5),
        'nbins': 100,
        'range': None
        })
])

settings['2.9'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.14, 0.18, 5),
        'bandwidth_adaptive': np.linspace(0.14, 0.18, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.21, 0.25, 5),
        'bandwidth_adaptive': np.linspace(0.21, 0.25, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.09, 0.13, 5),
        'bandwidth_adaptive': np.linspace(0.09, 0.13, 5),
        'nbins': 100,
        'range': None
        })
])

settings['3.0'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.12, 0.16, 5),
        'bandwidth_adaptive': np.linspace(0.12, 0.16, 5),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.15, 0.19, 5),
        'bandwidth_adaptive': np.linspace(0.15, 0.19, 5),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.12, 0.16, 5),
        'bandwidth_adaptive': np.linspace(0.12, 0.16, 5),
        'nbins': 100,
        'range': None
        })
])

settings['3.5'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.11, 11),
        'bandwidth_adaptive': np.linspace(0.01, 0.11, 11),
        'nbins': 100,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth_binned': np.linspace(0.06, 0.16, 11),
        'bandwidth_adaptive': np.linspace(0.06, 0.16, 11),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.11, 11),
        'bandwidth_adaptive': np.linspace(0.01, 0.11, 11),
        'nbins': 100,
        'range': None
        })
])

grid = None
