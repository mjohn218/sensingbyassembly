#!/bin/bash
#SBATCH --job-name=KdL100_F12
#SBATCH --time=72:0:0
#SBATCH --partition=parallel
#SBATCH --nodes=1
# number of tasks (processes) per node
#SBATCH --ntasks-per-node=48
#SBATCH --account=mjohn218

ml gsl

dirs=(15 30 45 60 75 90 105 120 135 150 165 180)
for dir in ${dirs[@]}; do
    cd $dir
    subdirs=$(ls -d */ 2>/dev/null)
    for sdir in $subdirs; do
        cd $sdir
        ./../../nerdss -f parms.inp >output.txt 2>&1 &
        cd ..
    done
    cd ..
done

wait
