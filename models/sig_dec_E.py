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
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.concatenate((np.linspace(0.52, 0.54, 2),
                                     np.linspace(0.58, 0.60, 2))),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['1.5'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.60, 0.80, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.0'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.30, 0.50, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.1'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.20, 0.40, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.2'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.05, 0.25, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.3'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.05, 0.25, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.4'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.05, 0.25, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.5'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.05, 0.25, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.6'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.05, 0.25, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.7'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.05, 0.25, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.8'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.05, 0.25, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['2.9'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.05, 0.25, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

settings['3.0'] = OrderedDict([
    ('sigma_pull_corrected', {
        'values': "np.log10(mc['sigma_pull_corrected'])",
        'bandwidth': np.linspace(0.05, 0.30, 6),
        'nbins': 100,
        'range': "[np.min(np.log10(mc['sigma_pull_corrected']))-0.5, \
                   np.max(np.log10(mc['sigma_pull_corrected']))+0.5]"
        }),
    ('true_dec', {
        'values': "np.sin(mc['true_dec'])",
        'bandwidth': np.linspace(0.01, 0.09, 5),
        'nbins': 100,
        'range': [np.sin(np.radians(-5)), 1.0]
        }),
    ('log_e', {
        'values': "mc['log_e']",
        'bandwidth': np.linspace(0.05, 0.25, 5),
        'nbins': 100,
        'range': "[np.min(mc['log_e'])-0.5, np.max(mc['log_e'])+0.5]"
        })
])

grid = None
