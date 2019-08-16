# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = {}

settings['default'] = OrderedDict([
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

settings['1.5'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.15, 0.23, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.36, 0.44, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.66, 0.74, 5),
        'nbins': 150,
        'range': None
        })
])

settings['2.0'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.09, 0.17, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.32, 0.40, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.24, 0.32, 5),
        'nbins': 150,
        'range': None
        })
])

settings['2.1'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.09, 0.17, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.24, 0.32, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.24, 0.32, 5),
        'nbins': 150,
        'range': None
        })
])

settings['2.2'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.12, 0.20, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.24, 0.32, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.25, 0.33, 5),
        'nbins': 150,
        'range': None
        })
])

settings['2.3'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.12, 0.20, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.22, 0.30, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.22, 0.30, 5),
        'nbins': 150,
        'range': None
        })
])

settings['2.4'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.11, 0.19, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.24, 0.32, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.19, 0.27, 5),
        'nbins': 150,
        'range': None
        })
])

settings['2.5'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.12, 0.20, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.20, 0.28, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.15, 0.23, 5),
        'nbins': 150,
        'range': None
        })
])

settings['2.6'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.12, 0.20, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.20, 0.28, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.15, 0.23, 5),
        'nbins': 150,
        'range': None
        })
])

settings['2.7'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.08, 0.16, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.20, 0.28, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.11, 0.19, 5),
        'nbins': 150,
        'range': None
        })
])

settings['2.8'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.13, 0.21, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.22, 0.30, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.11, 0.19, 5),
        'nbins': 150,
        'range': None
        })
])

settings['2.9'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.13, 0.21, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.16, 0.24, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.11, 0.19, 5),
        'nbins': 150,
        'range': None
        })
])

settings['3.0'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.11, 0.19, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.18, 0.26, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.03, 0.11, 5),
        'nbins': 150,
        'range': None
        })
])

grid = None
