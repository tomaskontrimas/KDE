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
    args = parser.parse_args()
    return vars(args)

slurm_draft = """#!/usr/bin/env bash
#SBATCH --time=15:00
#SBATCH --mem=2000
#SBATCH --partition=kta
#SBATCH --error=/home/ge56lag/Software/KDE/output/slurm/slurm-%j.err
#SBATCH --output=/home/ge56lag/Software/KDE/output/slurm/slurm-%j.out

mkdir -p /home/ge56lag/Software/KDE/output/{model}/cv

python temp_python_{model}_{i}.py

cp "/var/tmp/cv_{i}.npy" /home/ge56lag/Software/KDE/output/{model}/cv

rm "/var/tmp/cv_{i}.npy"
rm temp_python_{model}_{i}.py
rm temp_submit_{model}_{i}.sub
"""

python_draft = """# -*- coding: utf-8 -*-

import numpy as np

from config import CFG
from kde_classes import Model, KDE

model = Model('models.{model}', mc=None, weighting=None)
kde = KDE(model)

result = kde.cross_validate({bandwidth}, adaptive={adaptive})

np.save("/var/tmp/cv_{i}.npy", result)
"""

# Set model and parameters.
args = parseArguments()
model = args['model']
adaptive = args['adaptive']

settings = importlib.import_module('models.{}'.format(model)).settings
bandwidths = [settings[key]['bandwidth'] for key in settings]

for i, bandwidth in enumerate(itertools.product(*bandwidths)):
    temp_submit = 'temp_submit_{model}_{i}.sub'.format(model=model, i=i)
    python_submit = 'temp_python_{model}_{i}.py'.format(model=model, i=i)

    with open(temp_submit, "w") as file:
        file.write(slurm_draft.format(model=model, i=i))

    with open(python_submit, "w") as file:
        file.write(python_draft.format(model=model,
                                       bandwidth=bandwidth,
                                       adaptive=adaptive,
                                       i=i))

    os.system("sbatch {}".format(temp_submit))
    sleep(0.0001)
