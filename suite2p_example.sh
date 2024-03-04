#!/bin/bash
#SBATCH --account=ctb-tim
#SBATCH --mem-per-cpu=64G

apptainer run -C -B .:/mnt -W ${SLURM_TMPDIR} suite2p_env.sif python /mnt/suite2p_example.py
sleep 1
