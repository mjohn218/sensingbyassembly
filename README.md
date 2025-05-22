# sensingbyassembly
This repository contains the template parameter file and setup script to generate input files to run a series of NERDSS simulations for surface self-assembly in the presence of receptors. The files here are for KdAA = 500 uM.

Usage:
```
python setup_runs.py <number_of_replicas>
```

This will create a subdirectory for each receptor copy number, and within each of those a subdirectory for each replica simulation. The directory 360 is an example of one of these subdirectories, showing the generated NERDSS input files in each replica subdirectory. Subdirectory 360/0/ contains example outputs from a NERDSS simulation run, showing the raw output data files from which the analyses are derived.

The runfirst12.sh and runlast12.sh bash scripts are example SLURM batch files for running all the generated simulations on a cluster, here tuned for the JHU Rockfish supercomputer. This assumes that one has already compiled NERDSS, and placed the executable in the parent directory.