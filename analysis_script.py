# -*- coding: utf-8 -*-

import numpy as np

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
