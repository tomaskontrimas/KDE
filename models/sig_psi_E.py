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
        'bandwidth': np.linspace(0.13, 0.21, 5),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.linspace(0.38, 0.46, 5),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.58, 0.66, 5),
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
        'bandwidth': np.concatenate((np.linspace(0.07, 0.09, 2),
                                     np.linspace(0.13, 0.15, 2))),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.concatenate((np.linspace(0.26, 0.28, 2),
                                     np.linspace(0.32, 0.34, 2))),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.18, 0.20, 2),
                                     np.linspace(0.24, 0.26, 2))),
        'nbins': 150,
        'range': None
        })
])

settings['2.2'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.concatenate((np.linspace(0.06, 0.08, 2),
                                     np.linspace(0.12, 0.14, 2))),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.concatenate((np.linspace(0.26, 0.28, 2),
                                     np.linspace(0.32, 0.34, 2))),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.19, 0.21, 2),
                                     np.linspace(0.25, 0.27, 2))),
        'nbins': 150,
        'range': None
        })
])

settings['2.3'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.concatenate((np.linspace(0.06, 0.08, 2),
                                     np.linspace(0.12, 0.14, 2))),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.concatenate((np.linspace(0.22, 0.24, 2),
                                     np.linspace(0.28, 0.30, 2))),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.16, 0.18, 2),
                                     np.linspace(0.22, 0.24, 2))),
        'nbins': 150,
        'range': None
        })
])

settings['2.4'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.concatenate((np.linspace(0.05, 0.07, 2),
                                     np.linspace(0.11, 0.13, 2))),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.concatenate((np.linspace(0.22, 0.24, 2),
                                     np.linspace(0.28, 0.30, 2))),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.13, 0.15, 2),
                                     np.linspace(0.19, 0.21, 2))),
        'nbins': 150,
        'range': None
        })
])

settings['2.5'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.concatenate((np.linspace(0.06, 0.08, 2),
                                     np.linspace(0.12, 0.14, 2))),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.concatenate((np.linspace(0.26, 0.28, 2),
                                     np.linspace(0.32, 0.34, 2))),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.09, 0.11, 2),
                                     np.linspace(0.15, 0.17, 2))),
        'nbins': 150,
        'range': None
        })
])

settings['2.6'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.concatenate((np.linspace(0.06, 0.08, 2),
                                     np.linspace(0.12, 0.14, 2))),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.concatenate((np.linspace(0.26, 0.28, 2),
                                     np.linspace(0.32, 0.34, 2))),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.09, 0.11, 2),
                                     np.linspace(0.15, 0.17, 2))),
        'nbins': 150,
        'range': None
        })
])

settings['2.7'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.concatenate((np.linspace(0.06, 0.08, 2),
                                     np.linspace(0.12, 0.14, 2))),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.concatenate((np.linspace(0.26, 0.28, 2),
                                     np.linspace(0.32, 0.34, 2))),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.09, 0.11, 2),
                                     np.linspace(0.15, 0.17, 2))),
        'nbins': 150,
        'range': None
        })
])

settings['2.8'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.concatenate((np.linspace(0.07, 0.09, 2),
                                     np.linspace(0.13, 0.15, 2))),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.concatenate((np.linspace(0.24, 0.26, 2),
                                     np.linspace(0.30, 0.32, 2))),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.05, 0.07, 2),
                                     np.linspace(0.11, 0.13, 2))),
        'nbins': 150,
        'range': None
        })
])

settings['2.9'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.concatenate((np.linspace(0.07, 0.09, 2),
                                     np.linspace(0.13, 0.15, 2))),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.concatenate((np.linspace(0.22, 0.24, 2),
                                     np.linspace(0.28, 0.30, 2))),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.05, 0.07, 2),
                                     np.linspace(0.11, 0.13, 2))),
        'nbins': 150,
        'range': None
        })
])

settings['3.0'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.concatenate((np.linspace(0.05, 0.07, 2),
                                     np.linspace(0.11, 0.13, 2))),
        'nbins': 150,
        'range': None
        }),
    ('psi', {
        'values': "np.log10(mc['psi'])",
        'bandwidth': np.concatenate((np.linspace(0.24, 0.26, 2),
                                     np.linspace(0.30, 0.32, 2))),
        'nbins': 300,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.05, 0.07, 2),
                                     np.linspace(0.11, 0.13, 2))),
        'nbins': 150,
        'range': None
        })
])

grid = None
