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

mkdir -p /home/ge56lag/Software/KDE/output/{model}/pdf

python temp_python_{model}.py

cp /var/tmp/{model}.pkl /home/ge56lag/Software/KDE/output/{model}/pdf

rm /var/tmp/{model}.pkl
rm temp_python_{model}.py
rm temp_local_{model}.sh
"""

slurm_draft = """#!/usr/bin/env bash
#SBATCH --time=3:00:00
#SBATCH --mem=2000
#SBATCH --partition=kta
#SBATCH --error=/home/ge56lag/Software/KDE/output/slurm/slurm-%j.err
#SBATCH --output=/home/ge56lag/Software/KDE/output/slurm/slurm-%j.out

mkdir -p /home/ge56lag/Software/KDE/output/{model}/pdf

python temp_python_{model}.py

cp /var/tmp/{model}.pkl /home/ge56lag/Software/KDE/output/{model}/pdf

rm /var/tmp/{model}.pkl
rm temp_python_{model}.py
rm temp_slurm_{model}.sub
"""

python_draft = """# -*- coding: utf-8 -*-

import cPickle as pickle
import glob
import itertools
import numpy as np
import os.path

from kde_classes import Model, KDE

model = Model('{model}', mc=None, weighting='{weighting}',
              gamma={gamma}, phi0={phi0})
kde = KDE(model)

cv_files = glob.glob('output/{model}/cv/cv_*.npy')
cv_results = np.array([], dtype=kde.cv_result.dtype)

for cv_file in cv_files:
    cv_result = np.load(cv_file)
    cv_results = np.append(cv_results, cv_result)

cv_results_max_LLH = cv_results[cv_results['LLH'] == np.max(cv_results['LLH'])]

bandwidth = [cv_results_max_LLH[key] for key in model.bandwidth_vars]

if {adaptive}:
    kernel_density = kde.generate_adaptive_kd(bandwidth)
else:
    kernel_density = kde.generate_binned_kd(bandwidth)

out_bins, coords, pdf_vals = kde.get_bins_coordinates_and_pdf_values(kernel_density)

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
weighting = args['weighting']
gamma = args['gamma']
phi0 = args['phi0']
local = args['local']

temp_python_ = 'temp_python_{model}.py'.format(model=model)

with open(temp_python_, "w") as file:
    file.write(python_draft.format(model=model,
                                   weighting=weighting,
                                   gamma=gamma,
                                   phi0=phi0,
                                   adaptive=adaptive))
if local:
    temp_local = 'temp_local_{model}.sh'.format(model=model)
    with open(temp_local, "w") as file:
        file.write(local_draft.format(model=model))

    os.system("source ./{}".format(temp_local))
else:
    temp_slurm = 'temp_slurm_{model}.sub'.format(model=model)
    with open(temp_slurm, "w") as file:
        file.write(slurm_draft.format(model=model))

    os.system("sbatch {}".format(temp_slurm))
