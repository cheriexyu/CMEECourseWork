#!/bin/bash

python3 data_wrangle.py
python3 sample.py
python3 AIC.py
Rscript example_plot.R
Rscript AIC_summary.R
source bash.sh
echo "Compiling LaTex into Report.pdf"
