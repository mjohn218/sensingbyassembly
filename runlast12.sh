#!/bin/bash
#SBATCH --job-name=KdL100_L12
#SBATCH --time=72:0:0
#SBATCH --partition=parallel
#SBATCH --nodes=1
# number of tasks (processes) per node
#SBATCH --ntasks-per-node=48
#SBATCH --account=mjohn218

ml gsl

dirs=(195 210 225 240 255 270 285 300 315 330 345 360)
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
