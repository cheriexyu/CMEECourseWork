#!/bin/bash
#PBS -l walltime=12:00:00 
#PBS -l select=1:ncpus=1:mem=1gb
cp $HOME/cy221_HPC_2021_main.R $TMPDIR
module load anaconda3/personal
echo "R is about to run"
R --vanilla <$HOME/cluster.R 
mv cy221_cluster_run* $HOME 
echo "R has finished running"
