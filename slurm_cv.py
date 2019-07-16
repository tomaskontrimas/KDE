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

# slurm_draft = '#!/usr/bin/env bash \n\
# #SBATCH --time=2:30:00 \n\
# #SBATCH --mem=8000 \n\
# #SBATCH --partition=kta \n\
# #SBATCH --error={bpath}/slurm.err \n\
# #SBATCH --output={bpath}/slurm.out \n\
# bash ./env.sh {args}\n'

#SBATCH --error=/home/ge56lag/Software/KDE/output/{model}/slurm/slurm.err
#SBATCH --output=/home/ge56lag/Software/KDE/output/{model}/slurm/slurm.out

slurm_draft = """#!/usr/bin/env bash

mkdir -p /home/ge56lag/Software/KDE/output/{model}/slurm
mkdir -p /home/ge56lag/Software/KDE/output/{model}/cv

python temp_python_{i}.py

cp "/var/tmp/cv_{i}.npy" /home/ge56lag/Software/KDE/output/{model}/cv

rm temp_python_{i}.py
"""

python_draft = """# -*- coding: utf-8 -*-

import numpy as np

from config import CFG
from kde_classes import Model, KDE

model = Model('models.{model}', mc=None, weighting=None)
kde = KDE(model)

result = kde.cross_validate({bandwidth}, {adaptive})

np.save("/var/tmp/cv_{i}.npy", result)
"""

# Set model and parameters.
args = parseArguments()
model = args['model']
adaptive = args['adaptive']

print(model)
print(adaptive)

settings = importlib.import_module('models.{}'.format(model)).settings
bandwidths = [settings[key]['bandwidth'] for key in settings]

for i, bandwidth in enumerate(itertools.product(*bandwidths)):
    temp_submit = 'temp_submit.sub'
    python_submit = 'temp_python_{i}.py'.format(i=i)

    with open(temp_submit, "w") as file:
        file.write(slurm_draft.format(model=model, i=i))

    with open(python_submit, "w") as file:
        file.write(python_draft.format(model=model,
                                       bandwidth=bandwidth,
                                       adaptive=adaptive,
                                       i=i))

    os.system("sbatch {}".format(temp_submit))
    sleep(0.0001)
