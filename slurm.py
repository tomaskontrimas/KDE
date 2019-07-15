# -*- coding: utf-8 -*-

import importlib
import itertools
import os
from time import sleep

# slurm_draft = '#!/usr/bin/env bash \n\
# #SBATCH --time=2:30:00 \n\
# #SBATCH --mem=8000 \n\
# #SBATCH --partition=kta \n\
# #SBATCH --error={bpath}/slurm.err \n\
# #SBATCH --output={bpath}/slurm.out \n\
# bash ./env.sh {args}\n'

slurm_draft = """#!/usr/bin/env bash

#SBATCH --error=/home/ge56lag/Software/KDE/output/{model}/slurm/slurm.err
#SBATCH --output=/home/ge56lag/Software/KDE/output/{model}/slurm/slurm.out

mkdir -p /home/ge56lag/Software/KDE/output/{model}/slurm

python temp_python.py

cp "/var/tmp/cv_{bw_str}.txt" /home/ge56lag/Software/KDE/output/{model}
"""

python_draft = """# -*- coding: utf-8 -*-

import numpy as np

from config import CFG
from dataset import load_and_prepare_data
from kde_classes import Model, KDE

mc = np.load(CFG['paths']['mg_mc'])

model = Model('{model_module}', mc, weighting=None)
kde = KDE(model)

result = kde.cross_validate({bandwidth}, {adaptive})

with open("/var/tmp/cv_{bw_str}.txt","w") as f:
    f.write(str(result))
"""

# Set model and parameters.
model = 'multi_gaussian'
adaptive = False

settings = importlib.import_module('models.{}'.format(model)).settings
bandwidths = [settings[key]['bandwidth'] for key in settings]

for bandwidth in itertools.product(*bandwidths):
    temp_submit = 'temp_submit.sub'
    python_submit = 'temp_python.py'

    with open(temp_submit, "w") as file:
        file.write(slurm_draft.format(model=model, bw_str=str(bandwidth)))

    with open(python_submit, "w") as file:
        file.write(python_draft.format(model_module='models.{}'.format(model),
                                       bandwidth=bandwidth,
                                       adaptive=adaptive,
                                       bw_str=str(bandwidth)))

    os.system("sbatch {}".format(temp_submit))
    sleep(0.0001)
