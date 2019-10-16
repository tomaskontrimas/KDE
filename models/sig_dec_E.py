# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

settings = {}

settings['default'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.17, 0.23, 7),
        'bandwidth_adaptive': np.linspace(0.17, 0.23, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.07, 0.11, 5),
        'bandwidth_adaptive': np.linspace(0.07, 0.11, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.72, 0.82, 6),
        'bandwidth_adaptive': np.linspace(0.72, 0.82, 6),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['1.50'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.17, 0.23, 7),
        'bandwidth_adaptive': np.linspace(0.17, 0.23, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.07, 0.11, 5),
        'bandwidth_adaptive': np.linspace(0.07, 0.11, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.72, 0.82, 6),
        'bandwidth_adaptive': np.linspace(0.72, 0.82, 6),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.00'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.14, 0.20, 7),
        'bandwidth_adaptive': np.linspace(0.14, 0.20, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.03, 0.07, 5),
        'bandwidth_adaptive': np.linspace(0.03, 0.07, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.32, 0.42, 6),
        'bandwidth_adaptive': np.linspace(0.32, 0.42, 6),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.10'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.14, 0.20, 7),
        'bandwidth_adaptive': np.linspace(0.14, 0.20, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.03, 0.07, 5),
        'bandwidth_adaptive': np.linspace(0.03, 0.07, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.32, 0.42, 6),
        'bandwidth_adaptive': np.linspace(0.32, 0.42, 6),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.20'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.21, 7),
        'bandwidth_adaptive': np.linspace(0.15, 0.21, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.01, 0.05, 5),
        'bandwidth_adaptive': np.linspace(0.01, 0.05, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 6),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.30'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.17, 0.23, 7),
        'bandwidth_adaptive': np.linspace(0.17, 0.23, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.01, 0.05, 5),
        'bandwidth_adaptive': np.linspace(0.01, 0.05, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 6),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.40'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.17, 0.23, 7),
        'bandwidth_adaptive': np.linspace(0.17, 0.23, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.01, 0.05, 5),
        'bandwidth_adaptive': np.linspace(0.01, 0.05, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 6),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.50'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.17, 0.23, 7),
        'bandwidth_adaptive': np.linspace(0.17, 0.23, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.01, 0.05, 5),
        'bandwidth_adaptive': np.linspace(0.01, 0.05, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.20, 0.30, 6),
        'bandwidth_adaptive': np.linspace(0.20, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.60'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.17, 0.23, 7),
        'bandwidth_adaptive': np.linspace(0.17, 0.23, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.01, 0.05, 5),
        'bandwidth_adaptive': np.linspace(0.01, 0.05, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.16, 0.22, 7),
        'bandwidth_adaptive': np.linspace(0.16, 0.22, 7),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.70'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.15, 0.21, 7),
        'bandwidth_adaptive': np.linspace(0.15, 0.21, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.01, 0.05, 5),
        'bandwidth_adaptive': np.linspace(0.01, 0.05, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.16, 0.22, 7),
        'bandwidth_adaptive': np.linspace(0.16, 0.22, 7),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.80'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.16, 0.22, 7),
        'bandwidth_adaptive': np.linspace(0.16, 0.22, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.01, 0.05, 5),
        'bandwidth_adaptive': np.linspace(0.01, 0.05, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.15, 0.21, 7),
        'bandwidth_adaptive': np.linspace(0.15, 0.21, 7),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.90'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.16, 0.22, 7),
        'bandwidth_adaptive': np.linspace(0.16, 0.22, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.01, 0.05, 5),
        'bandwidth_adaptive': np.linspace(0.01, 0.05, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.12, 0.18, 7),
        'bandwidth_adaptive': np.linspace(0.12, 0.18, 7),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['3.00'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.16, 0.22, 7),
        'bandwidth_adaptive': np.linspace(0.16, 0.22, 7),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.01, 0.05, 5),
        'bandwidth_adaptive': np.linspace(0.01, 0.05, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.12, 0.18, 7),
        'bandwidth_adaptive': np.linspace(0.12, 0.18, 7),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['3.50'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth_binned': np.linspace(0.05, 0.15, 11),
        'bandwidth_adaptive': np.linspace(0.05, 0.15, 11),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth_binned': np.linspace(0.005, 0.05, 10),
        'bandwidth_adaptive': np.linspace(0.005, 0.05, 10),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth_binned': np.linspace(0.08, 0.18, 11),
        'bandwidth_adaptive': np.linspace(0.08, 0.18, 11),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

grid = None
