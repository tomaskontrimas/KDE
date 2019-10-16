# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = {}

settings['default'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.70, 70),
        'bandwidth_adaptive': np.linspace(0.01, 0.70, 70),
        'nbins': 100,
        'range': None
        })
])

settings['1.50'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.30, 0.70, 41),
        'bandwidth_adaptive': np.linspace(0.30, 0.70, 41),
        'nbins': 100,
        'range': None
        })
])

settings['2.00'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.20, 20),
        'bandwidth_adaptive': np.linspace(0.01, 0.20, 20),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        })
])

settings['2.10'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.20, 20),
        'bandwidth_adaptive': np.linspace(0.01, 0.20, 20),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        })
])

settings['2.20'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.20, 20),
        'bandwidth_adaptive': np.linspace(0.01, 0.20, 20),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        })
])

settings['2.30'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.20, 20),
        'bandwidth_adaptive': np.linspace(0.01, 0.20, 20),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        })
])

settings['2.40'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.20, 20),
        'bandwidth_adaptive': np.linspace(0.01, 0.20, 20),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        })
])

settings['2.50'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.20, 20),
        'bandwidth_adaptive': np.linspace(0.01, 0.20, 20),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        })
])

settings['2.60'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.20, 20),
        'bandwidth_adaptive': np.linspace(0.01, 0.20, 20),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        })
])

settings['2.70'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.20, 20),
        'bandwidth_adaptive': np.linspace(0.01, 0.20, 20),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        })
])

settings['2.80'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.20, 20),
        'bandwidth_adaptive': np.linspace(0.01, 0.20, 20),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        })
])

settings['2.90'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.20, 20),
        'bandwidth_adaptive': np.linspace(0.01, 0.20, 20),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        })
])

settings['3.00'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.01, 0.20, 20),
        'bandwidth_adaptive': np.linspace(0.01, 0.20, 20),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.01, 0.30, 30),
        'bandwidth_adaptive': np.linspace(0.01, 0.30, 30),
        'nbins': 100,
        'range': None
        })
])

settings['3.50'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.005, 0.06, 12),
        'bandwidth_adaptive': np.linspace(0.005, 0.06, 12),
        'nbins': 100,
        'range': None
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.03, 0.09, 13),
        'bandwidth_adaptive': np.linspace(0.03, 0.09, 13),
        'nbins': 100,
        'range': None
        })
])

grid = None
