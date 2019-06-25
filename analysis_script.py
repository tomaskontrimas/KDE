# -*- coding: utf-8 -*-

from config import CFG
from dataset import load_and_prepare_data
from kde_classes import Model, KDE

from models.example_new import settings, grid

mc = load_and_prepare_data(CFG['paths']['IC_mc'])

model = Model(mc, settings)

kde = KDE(model, adaptive=False)

binned_kernel_density = kde.generate_binned_kernel_density()

print(kde.eval_point([0.1, 0.1, 0.1]))
