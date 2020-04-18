import os, sys
import glob 
os.chdir('_new')

apsim_files = glob.glob("./*.apsim")
for file in apsim_files :
    os.system("apsim "+file)
