# -*- coding: utf-8 -*-

import numpy as np
import itertools

from config import CFG
from dataset import load_and_prepare_data
from kde_classes import Model, KDE

#from models.example_new import settings, grid
from models.multi_gaussian import settings, grid

#mc = load_and_prepare_data(CFG['paths']['IC_mc'])

mg = np.load(CFG['paths']['mg_mc'])

# model = Model(mc, settings)
model = Model(mg, settings)

kde = KDE(model, adaptive=False)

binned_kernel_density = kde.generate_binned_kernel_density()

print(kde.eval_point([0, 0]))


out_bins = []
for key in settings:
    out_bins.append([np.linspace(settings[key]['range'][0],
                                 settings[key]['range'][1],
                                 settings[key]['nbins'])])

print(out_bins)

coords = np.array(list(itertools.product(*out_bins)))

print(coords)

print('Evaluate KDEs:')
pdf_vals = np.asarray([kde.eval_point(coord) for coord in coords])
shpe = np.ones(len(settings.keys()), dtype=int) * nbins
pdf_vals = pdf_vals.reshape(*shpe)

print(pdf_vals)
