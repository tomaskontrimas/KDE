# -*- coding: utf-8 -*-

import argparse
import importlib
import itertools
import os

from config import CFG

def parseArguments():
    """Parse the command line arguments.

    Returns
    -------
    args : dict
        Dictionary containing the command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "model", type=str)
    parser.add_argument(
        "--adaptive", action="store_true", default=False)
    parser.add_argument(
        "--partition", type=str, default='kta')
    parser.add_argument(
        "--time", type=str, default='3:00:00')
    parser.add_argument(
        "--weighting", type=str, default=None)
    parser.add_argument(
        "--gamma", type=float, default=2.0)
    parser.add_argument(
        "--phi0", type=float, default=1.0)
    parser.add_argument(
        "--local", action="store_true", default=False)
    parser.add_argument(
        "--split", action="store_true", default=False)
    parser.add_argument(
        "--seed", action="store_true", default=False)
    args = parser.parse_args()
    return vars(args)

local_draft = """#!/usr/bin/env bash

mkdir -p {working_directory}/output/{model}/{parameters_dir}/cv

python temp_python_{seed_str}{model}_{parameters_dir}_{i}_{n_split}.py

mv /var/tmp/cv_{i}_{n_split}.npy {working_directory}/output/{model}/{parameters_dir}/cv/cv_{bw_str}_{n_split}.npy

#rm /var/tmp/cv_{i}_{n_split}.npy
rm temp_python_{seed_str}{model}_{parameters_dir}_{i}_{n_split}.py
rm temp_local_{seed_str}{model}_{parameters_dir}_{i}_{n_split}.sh
"""

slurm_draft = """#!/usr/bin/env bash

#SBATCH --time={time}
#SBATCH --mem=2000
#SBATCH --partition={partition}
#SBATCH --error={working_directory}/output/slurm/slurm-%j.err
#SBATCH --output={working_directory}/output/slurm/slurm-%j.out

mkdir -p {working_directory}/output/{model}/{parameters_dir}/cv

python temp_python_{seed_str}{model}_{parameters_dir}_{i}_{n_split}.py

if {seed}; then
    mv /var/tmp/cv_seed_{model}_{bw_str}_{n_split}.txt {working_directory}/output/{model}/{parameters_dir}/cv/cv_seed_{model}_{bw_str}_{n_split}.txt
else
    mv /var/tmp/cv_{i}_{n_split}.npy {working_directory}/output/{model}/{parameters_dir}/cv/cv_{bw_str}_{n_split}.npy
fi

rm temp_python_{seed_str}{model}_{parameters_dir}_{i}_{n_split}.py
rm temp_slurm_{seed_str}{model}_{parameters_dir}_{i}_{n_split}.sub
"""

python_draft = """# -*- coding: utf-8 -*-

import os
import logging
import numpy as np
import time
from datetime import timedelta

# Logging setup utilities
from debugging import (
    setup_logger,
    setup_console_handler
)

from kde_classes import Model, KDE

setup_logger('KDE', logging.DEBUG)
setup_console_handler('KDE', logging.DEBUG)
logger = logging.getLogger('KDE.' + __name__)

start_time = time.time()

model = Model('{model}', mc=None, weighting='{weighting}',
              gamma={gamma}, phi0={phi0})
kde = KDE(model)

if {seed}:
    if {split}:
        kde.set_kfold_subset({n_split})
        binned_kernel = kde.generate_binned_kd({bandwidth})
    else:
        binned_kernel = kde.generate_binned_kd({bandwidth})

    binned_kernel.writeToFile('/var/tmp/cv_seed_{model}_{bw_str}_{n_split}.txt')
else:
    seed_path = '{working_directory}/output/{model}/{parameters_dir}/cv/cv_seed_{model}_{bw_str}_{n_split}.txt'
    if os.path.exists(seed_path):
        pdf_seed = BinnedDensity.readFromFile(seed_path)
    else:
        pdf_seed = None

    if {split}:
        result = kde.cross_validate_split({bandwidth}, {n_split},
            adaptive={adaptive}, pdf_seed=pdf_seed)
    else:
        result = kde.cross_validate({bandwidth}, adaptive={adaptive},
                                    pdf_seed=pdf_seed)

    np.save("/var/tmp/cv_{i}_{n_split}.npy", result)

elapsed_time = time.time() - start_time
logger.debug('Elapsed time %s', timedelta(seconds=elapsed_time))
"""

# Set model and parameters.
args = parseArguments()
model = args['model']
adaptive = args['adaptive']
partition = args['partition']
time = args['time']
weighting = args['weighting']
gamma = args['gamma']
phi0 = args['phi0']
local = args['local']
split = args['split']
seed = args['seed']

if seed:
    seed_str = 'seed_'
else:
    seed_str = ''

working_directory = CFG['project']['working_directory']

parameters_dir_format = '{kd}_{weighting}_gamma_{gamma}_phi0_{phi0}'
parameters_dir = parameters_dir_format.format(kd='adaptive_kd' if adaptive else
    'binned_kd', weighting=weighting, gamma=gamma, phi0=phi0)

settings = importlib.import_module('models.{}'.format(model)).settings[str(gamma)]
bandwidths = [settings[key]['bandwidth'] for key in settings]

for i, bandwidth in enumerate(itertools.product(*bandwidths)):
    bw_str = ','.join(map('{:.3f}'.format, bandwidth))
    if split:
        n_splits = CFG['project']['n_splits']
    else:
        n_splits = 1

    for n_split in range(n_splits):
        python_submit = 'temp_python_{seed_str}{model}_{par_dir}_{i}_{n_split}'\
            '.py'.format(seed_str=seed_str, model=model, par_dir=parameters_dir,
            i=i, n_split=n_split)
        with open(python_submit, "w") as file:
            file.write(python_draft.format(seed=seed,
                                           model=model,
                                           weighting=weighting,
                                           gamma=gamma,
                                           phi0=phi0,
                                           bandwidth=bandwidth,
                                           bw_str=bw_str,
                                           adaptive=adaptive,
                                           i=i,
                                           working_directory=working_directory,
                                           parameters_dir=parameters_dir,
                                           n_split=n_split,
                                           split=split))

        if local:
            temp_local = 'temp_local_{seed_str}{model}_{par_dir}_{i}_{n_split}'\
                '.sh'.format(seed_str=seed_str, model=model,
                             par_dir=parameters_dir, i=i, n_split=n_split)
            with open(temp_local, "w") as file:
                file.write(local_draft.format(seed=str(seed).lower(),
                                              seed_str=seed_str,
                                              model=model,
                                              i=i,
                                              working_directory=working_directory,
                                              parameters_dir=parameters_dir,
                                              n_split=n_split,
                                              bw_str=bw_str))

            os.system("source ./{}".format(temp_local))
        else:
            temp_slurm = 'temp_slurm_{seed_str}{model}_{par_dir}_{i}_{n_split}'\
            '.sub'.format(seed_str=seed_str, model=model,
                          par_dir=parameters_dir, i=i, n_split=n_split)
            with open(temp_slurm, "w") as file:
                file.write(slurm_draft.format(seed=str(seed).lower(),
                                              seed_str=seed_str,
                                              model=model,
                                              i=i,
                                              working_directory=working_directory,
                                              parameters_dir=parameters_dir,
                                              n_split=n_split,
                                              bw_str=bw_str,
                                              partition=partition,
                                              time=time))

            os.system("sbatch {}".format(temp_slurm))
