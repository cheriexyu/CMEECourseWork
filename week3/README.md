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
   - bash.sh : Bash program to run Florida_warming.tex script
   - Florida_warming.pdf : pdf result file for Florida_warming.R code pratical
   - Florida_warming.tex : LaTex source codes to producing a pdf results file (Florida_warming.pdf)
   - Groupwork Practicals
        - get_TreeHeight.R
        - get_TreeHeight.py
        - run_get_TreeHeight.sh
        - TAutoCorr.R
        - TAutoCorr.tex
        - CompileLaTeX.sh

../data

../results

../sandbox


Author: Cherie Yu

Contact: cyy21@ic.ac.uk
