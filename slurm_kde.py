# -*- coding: utf-8 -*-

import argparse
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

slurm_draft = """#!/usr/bin/env bash

#SBATCH --error="/home/ge56lag/Software/KDE/output/slurm/slurm-%j.err"
#SBATCH --output="/home/ge56lag/Software/KDE/output/slurm/slurm-%j.out"

mkdir -p /home/ge56lag/Software/KDE/output/{model}/KDE

python temp_python.py

cp "/var/tmp/{model}.pkl" /home/ge56lag/Software/KDE/output/{model}/KDE

rm temp_python.py
"""

python_draft = """# -*- coding: utf-8 -*-

import cPickle as pickle
import glob
import itertools
import numpy as np
import os.path

from config import CFG
from kde_classes import Model, KDE

model = Model('models.{model}', mc=None, weighting=None)
kde = KDE(model)

cv_files = glob.glob('output/{model}/cv/cv_*.npy')
cv_results = np.array([], dtype=kde.cv_result.dtype)

for cv_file in cv_files:
    cv_result = np.load(cv_file)
    cv_results = np.append(cv_results, cv_result)

result_max_LLH = cv_results[cv_results['LLH'] == np.max(cv_results['LLH'])]

bandwidth = [result_max_LLH[key] for key in model.bandwidth_vars]

if {adaptive}:
    kernel_density = kde.generate_adaptive_kd(bandwidth)
else:
    kernel_density = kde.generate_binned_kd(bandwidth)

out_bins = []
for i, key in enumerate(kde.model.vars):
    out_bins.append(np.linspace(kde.model.ranges[i][0],
                            kde.model.ranges[i][1],
                            kde.model.nbins[i]))
coords = np.array(list(itertools.product(*out_bins)))
pdf_vals = np.asarray(
    [kde.eval_point(kernel_density, coord) for coord in coords])
pdf_vals = pdf_vals.reshape(kde.model.nbins)

result_dict = {{
    'vars': kde.model.vars,
    'bins': out_bins,
    'coords': coords,
    'pdf_vals': pdf_vals,
    'bw': bandwidth
}}

with open(os.path.join('/var/tmp/{model}.pkl'), 'wb') as file:
            pickle.dump(result_dict, file)
"""

# Set model and parameters.
args = parseArguments()
model = args['model']
adaptive = args['adaptive']

temp_submit = 'temp_submit.sub'
python_submit = 'temp_python.py'

with open(temp_submit, "w") as file:
    file.write(slurm_draft.format(model=model))

with open(python_submit, "w") as file:
    file.write(python_draft.format(model=model, adaptive=adaptive))

os.system("sbatch {}".format(temp_submit))
