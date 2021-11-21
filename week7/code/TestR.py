#!/usr/bin/env python3
#############################
# Build Workflows, using ipython to open and run R script 
#############################

import subprocess

subprocess.Popen("Rscript --verbose TestR.R > ../Results/TestR.Rout 2> ../Results/TestR_errFile.Rout", shell=True).wait()
#Opens Rscript, saves the output into TestR.Rout and saves error into 2> 
#wait without a timeout argument will wait until process to complete 
