# *Week 3*


## General Description

Biological Computing in R - This week focuses on the use of R programming language in biology and the application to data management and visualization. 

***

## Languages
R 

***
## Dependencies
IDEs such as RStudio 

***
## Installation

Use the package manager [homebrew](https://brew.sh/) to install R and RStudio.

```bash
brew install r
```

```bash
brew install --cask rstudio
```

Package Installations in RStudio:

[tidyverse](https://www.tidyverse.org/) package in R includes the core packages ( tidyr, ggplot2, dplyr, readr, purrr, tibble, stringr, forcats)

```bash
install.packages("tidyverse")
```
    
[Reshape2](https://www.rdocumentation.org/packages/reshape2/versions/1.4.4) package in R.
    
```bash
install.packages("reshape2")
```

[Broom](https://broom.tidymodels.org/) package to summarize key information about models in R.

```bash
install.packages("broom")
```

```bash
#To load packages in R after installation:
library(#name of package)
```
***
## Project Structure and Usage

../code

   - basic_io.R : Runing input files and writing output files in R  
   - control_flow.R : Control flow statements in R (for loops, while loops)
   - break.R : Example of how to break out of a loop when a condition is met
   - next.R : Example of how to pass iteration to next loop
   - boilerplate.R : A boilerplate R script 
   - R_conditionals.R : Functions using conditional loops 
   - TreeHeight.R : Function calculates tree height, given the distance of each tree from the base and it's angle to the top 
   - Vectorize1.R : Vectorization in R
        - sample.R : Sample script of vectorization using apply functions 
        - apply*.R : R codes that show the use of apply family functions 
   - preallocate.R : Preallocating vectors to run functions efficectively in R
   - Vectorize2.R : Practical involving vectorizing the Ricker model (Ricker.R)
   - browse.R : Debugging in R
   - try.R : Catching errors in R using try command
   - Florida.R : Codes to "Is Florida Getting Warmer" Practical 
   - DataWrang.R : Codes for Data wrangling in R using example data
   - DataWrangTidy.R : Practical using tidyverse packages to wrangle data 
   - PP_Dists.R : Practical on body mass distributions in predator and prey
   - MyBars.R : Annotating plots using ggplot in R
   - plotLin.R : Annotating linear regression plots 
   - PP_Regress.R : Practical on visualizing regression analysis
   - CompileLaTeX.sh : Shell script to compile LaTeX documents 
   - Florida_warming.pdf : pdf result file for Florida_warming.R code pratical
   - Florida_warming.tex : LaTex source codes to producing a pdf results file (Florida_warming.pdf)
   - Groupwork Practicals
        - get_TreeHeight.R : Group script that calculates tree height and outputs into a output file name as InputFileName_treeheights.csv
        - get_TreeHeight.py : Python version of get_TreeHeight.R
        - run_get_TreeHeight.sh : Shell script to test get_TreeHeight.py
        - TAutoCorr.R : R script that answers the question "Are temperatures of one year significantly correlated with the next year (successive years), across years in a given location?"
        - TAutoCorr.tex : Results of TAutoCorr.R are presented in this LaTeX document  
        

../data

   - EcolArchives-E089-51-D1.csv : Dataset on consumer-resource body mass ratios from figshare (Barnes et al. 2008, Ecology 89:881)
   - GPDDFiltered.RData : Global Population Dynamics Database (GPDD) RData
   - KeyWestAnnualMeanTemperature.RData : Annual temperature dataset from Key West in Florida, USA for the 20th century
   - PoundHillData.csv : Dataset collected by students in past Silwood field course 
   - PoundHillMetaData.csv : Metadata file describing the data of PoundHillData.csv
   - Results.txt : Example data used for plotting in MyBars.R
   - trees.csv : Data of tree species, distance and height 

../results

../sandbox

***
Author: Cherie Yu

Contact: cyy21@ic.ac.uk
