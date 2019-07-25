# -*- coding: utf-8 -*-

import argparse
import importlib
import itertools
import os
from time import sleep

def parseArguments():
    """Parse the command line arguments
    Returns:
    args : Dictionary containing the command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "model", type=str)
    parser.add_argument(
        "--adaptive", action="store_true", default=False)
    parser.add_argument(
        "--weighting", type=str, default=None)
    parser.add_argument(
        "--gamma", type=float, default=2.0)
    parser.add_argument(
        "--phi0", type=float, default=1.01)
    parser.add_argument(
        "--local", action="store_true", default=False)
    args = parser.parse_args()
    return vars(args)

local_draft = """#!/usr/bin/env bash

mkdir -p /home/ge56lag/Software/KDE/output/{model}/cv

python temp_python_{model}_{i}.py

cp /var/tmp/cv_{i}.npy /home/ge56lag/Software/KDE/output/{model}/cv

rm /var/tmp/cv_{i}.npy
rm temp_python_{model}_{i}.py
rm temp_local_{model}_{i}.sh
"""

slurm_draft = """#!/usr/bin/env bash
#SBATCH --time=3:00:00
#SBATCH --mem=2000
#SBATCH --partition=kta
#SBATCH --error=/home/ge56lag/Software/KDE/output/slurm/slurm-%j.err
#SBATCH --output=/home/ge56lag/Software/KDE/output/slurm/slurm-%j.out

mkdir -p /home/ge56lag/Software/KDE/output/{model}/cv

python temp_python_{model}_{i}.py

cp /var/tmp/cv_{i}.npy /home/ge56lag/Software/KDE/output/{model}/cv

rm /var/tmp/cv_{i}.npy
rm temp_python_{model}_{i}.py
rm temp_slurm_{model}_{i}.sub
"""

python_draft = """# -*- coding: utf-8 -*-

import numpy as np

from kde_classes import Model, KDE

model = Model('{model}', mc=None, weighting='{weighting}',
              gamma={gamma}, phi0={phi0})
kde = KDE(model)

result = kde.cross_validate({bandwidth}, adaptive={adaptive})

np.save("/var/tmp/cv_{i}.npy", result)
"""

# Set model and parameters.
args = parseArguments()
model = args['model']
adaptive = args['adaptive']
weighting = args['weighting']
gamma = args['gamma']
phi0 = args['phi0']
local = args['local']

settings = importlib.import_module('models.{}'.format(model)).settings
bandwidths = [settings[key]['bandwidth'] for key in settings]

for i, bandwidth in enumerate(itertools.product(*bandwidths)):
    python_submit = 'temp_python_{model}_{i}.py'.format(model=model, i=i)

    with open(python_submit, "w") as file:
        file.write(python_draft.format(model=model,
                                       weighting=weighting,
                                       gamma=gamma,
                                       phi0=phi0,
                                       bandwidth=bandwidth,
                                       adaptive=adaptive,
                                       i=i))

    if local:
        temp_local = 'temp_local_{model}.sh'.format(model=model)
        with open(temp_local, "w") as file:
            file.write(local_draft.format(model=model, i=i))

        os.system("python {}".format(temp_local))
    else:
        temp_slurm = 'temp_slurm_{model}_{i}.sub'.format(model=model, i=i)
        with open(temp_slurm, "w") as file:
            file.write(slurm_draft.format(model=model, i=i))

        os.system("sbatch {}".format(temp_slurm))