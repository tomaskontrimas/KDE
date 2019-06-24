# -*- coding: utf-8 -*-

from config import CFG
from dataset import load_and_prepare_data

mc = load_and_prepare_data(CFG['paths']['IC_mc'])

print(mc)
