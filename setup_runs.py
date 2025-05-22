import os
import sys
import shutil
import numpy as np

# Generates folders and parms.inp files for
# varying concentrations of tfr. Copies
# mol files into each sim dir, and copies
# the run script into each conc dir

# expects as input the number of repeats of
# each simulation you want, e.g.
# python3 setup_runs.py 5

# get repeat num from user
n_repeat = int(sys.argv[1])

# fixed amount of A
# 0.2 uM (approx physiologic AP-2 conc)
numA = 120

# fixed value for now
koffAL = 30.0 # Kd ~ 100 uM

# fixed for these runs
konAA = 0.02 # uM^-1 s^-1
konAA_diff = 0.04

# receptor copy numbers
c1vals = [n for n in range(15,375,15)]

# mol files to copy into each dir
molfiles = ['A.mol','L.mol','c1.mol']

with open("template_parms.inp","r") as parms_template:
    parms_string = parms_template.read()

for c1 in c1vals:
    if not os.path.exists(str(c1)):
        os.makedirs(str(c1))
    
    with open(str(c1)+'/parms.inp','w') as parmfile:
        parmfile.write(parms_string.format(A=numA,c1=c1,koffAL=koffAL,konAA=konAA,konAA_diff=konAA_diff))
    
    for i in range(n_repeat):
        if not os.path.exists(str(c1)+'/'+str(i)):
            os.makedirs(str(c1)+'/'+str(i))
        
        shutil.copy(str(c1)+'/parms.inp',str(c1)+'/'+str(i)+'/parms.inp')
        
        for f in molfiles:
            shutil.copy(f,str(c1)+'/'+str(i)+'/'+f)



