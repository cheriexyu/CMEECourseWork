#!/bin/bash

python3 data_wrangle.py
echo "Data is being wrangled"
python3 sample.py
echo "Starting values are sampled"
echo "All plots can be found in graph directory"
python3 AIC.py
echo "AIC values are being calculated"
Rscript example_plot.R
Rscript AIC_summary.R
source bash.sh Report
echo "Compiling LaTex into Report.pdf"
