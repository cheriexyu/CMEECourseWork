# *MiniProject*


## General Description

The MiniProject aims to address the question: What mathematical models best fit an empirical dataset? The project I have choosen is based on applying phenomenolgical and mechanisitc mathematical models on to functional response data in bacterial species. This directory contains all codes, datas and the final output report within my investigation. 

***

## Languages
Python 3.9, R 4.1.2, Bash

***
## Dependencies
IDEs such as RStudio and Visual Studio Code 

***
## Installation
Here is a list of packages installed within each language during the coding process: 

Package Installations for use in Python 3.9 

[Numpy](https://numpy.org/) package allows for data creation, manipulation and undergoing basic arithemtic calculations within Python. 
Can use `pip` to install packages on bash terminal.  

```bash
pip3 install numpy
```
Note: `pip3` download packages directly into Python version 3.9

[Panda](https://pandas.pydata.org/docs/) package was widely used in my data wrangling and plotting phase. Panda is beneficial for creating and manipulating dataframes.

```bash
pip3 install pandas
```

[SciPy](https://scipy.org/) package is simillar to Numpy however it is recommended for more complex numerical operations. In the miniproject, the subpackages `scipy.stats`, `linregress` was mainly used. [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) allows you to undergo statistical analysis within Python (e.g correlation, probability distributions...). In my case, I used the [scipy.stats.linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html) function to calculate least square regression. 

```python
import scipy as sc
from scipy import stats 
from scipy.stats import linregress
```

[lmfit()](https://lmfit.github.io/lmfit-py/) In the main part of my project, I utilized the `lmfit` function for non-Linear least-squares minimization and curve-Fitting in Python. One of the key concepts in `lmfit` is the `Parameter` object. The parameter can be varied in a fit, you can add parameters into an equation or get minimzed parameters after model fitting. More information to this can be found [here](https://lmfit.github.io/lmfit-py/parameters.html#lmfit.parameter.Parameter). I applied this object to create starting values and used them for plotting my mathematical curves. The `minimize()` function was widely used during model fitting. The `minimize` function takes an objective function and it's parameters and minimize the fitting. I used the default leastsq Levenberg-Marquardt method. More information can be found [here](https://lmfit.github.io/lmfit-py/fitting.html#the-minimize-function). After minimization, to generate fitted results, use the function [`report_fit`](https://lmfit.github.io/lmfit-py/fitting.html#getting-and-printing-fit-reports). 

```bash
pip3 install lmfit
```
```python
from lmfit import Minimizer, Parameters, report_fit
```

[matplotlib](https://matplotlib.org/) library is used to create visualizations in Python. In my miniproject, I used `matplotlib` to generate plots. 
```bash
pip3 install matplotlib
```
Importing `matplotlib` to be used within the module `Pylab` (already embedded inside `matplotlib`) in Python:
```python
import matplotlib.pylab as pl
```   

Package Installations for use in R 4.1:

[tidyverse](https://www.tidyverse.org/) package in R includes the core packages ( tidyr, ggplot2, dplyr, readr, purrr, tibble, stringr, forcats). I used `ggplot` and `dplyr` to create plots in R, and `dplyr` to edit, filter and create dataframes. 

```bash
install.packages("tidyverse")
```

```r
library(dplyr)
```

In my report writing, I incoportaed an example plot of the sigmoid curve generated from R. To utilize a non-linear least square regression, the package `minpack.lm` was installed. The package is ran with the code `nlsLM()` using a modification of the Levenberg-Marquardt algorithm. More information is provided [here](https://cran.r-project.org/web/packages/minpack.lm/index.html)

```r
install.packages("minpack.lm")
```
To run non-linear least square regressions: 
```r
nlsLM()
```

## Project Structure and Usage

../code

   - run_MiniProject.sh : Bash script that runs all coding scripts in one go and outputs the report file called report.pdf 
   - bash.sh : Compiles the LaTeX script and bibliograph, outputs PDF file
   - Report.tex : LaTeX report on the MiniProject
   - miniproject.bib : Literature citations used in this project saved in BibTex file, ready to be used during compiling of the LaTeX
   - datawrangle.py : Data wrangling of the given data, sorting and manipulating data to be ready for model fitting 
   - sample.py : Python script that samples the starting parameters of the Gompertz equation, minimizes all the mathematical equations, and plots all graphs into the *graphs* directory. It also calculates the AIC values. 
   - AIC.py : Calculates the AICc values and all other statistics. Saves as output csv dataframes in *data* directory.
   - AIC_summary.R : Concatenates all AIC dataframes into one main script and output a final sorted dataframe for report writing.
   - example_plot.R : Plots a logistic sigmoid curve using random data, and saves as pdf in *graphs* directory. Used for report writing. 
   ../graphs : A folder directory containing all the plots, required for LaTex script

../data
   - LogiticGrowthData.csv : Dataset of the miniproject. It contains measurements of change in biomass or number of cells of microbes over time, done by experiements around the globe. 
   - LogisticGrowthMetaData.csv : The fieldnames of LogiticGrowthData.csv are defined here.
   - editeddata.csv : New dataset after data wrangling 
   - sample_size.csv : csv containing the sample size of each unique ID
   - minimized_paras_gompertz.csv : csv containing all the parameters and AIC for all datasets after model fitting and minimization of the Gompertz equation
   - AIC_output.csv : output of AIC values from all mathematical equations saved to a csv file
   - AICc_output.csv : output of AICc values from all mathematical equations saved to a csv file
   - scaled_aicc.csv : ∆AIC scores, further calculation of AICc scores, saved to a csv file
   - akaike_weight.csv : csv file containing the calculated akaike weights for all mathematical models across all datasets
   - AIC_final.csv : csv file containing all the fitted models across all datasets and their calculated AIC values
   - filtered_AIC_final.csv : csv file containing just the best fitted model across all datasets and their calculated AIC values

Author: Cherie Yu
Contact: cyy21@ic.ac.uk
