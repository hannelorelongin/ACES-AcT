#!/bin/bash

#SBATCH --nodes=1 --ntasks-per-node=8
#SBATCH --time=00:15:00

cd $SLURM_SUBMIT_DIR

source /data/leuven/331/vsc33164/miniconda3/bin/activate
conda activate lovis4u

lovis4u --linux

lovis4u -gb ./gb/ -o full_genomes -rol -hl


