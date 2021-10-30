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

Use the package manager [homebrew] (https://brew.sh/) to install R and RStudio.

```bash
brew install r
```

```bash
brew install --cask rstudio
```

Package Installations in RStudio:

    tidyverse package in R [Link to more information] (https://www.tidyverse.org/) includes the core packages (ggplot2,dplyr,readr,purrr,tibble,stringr,forcats)

    ```r
    install.packages("tidyverse")
    ```
    
    Reshape2 package in R [Link to more information] (https://www.rdocumentation.org/packages/reshape2/versions/1.4.4)
    
    ```r
    install.packages("reshape2")
    ```

    ```r
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

../LaTex

   - bash.sh : Bash program to run Floridaoutput.tex script
   - Floridaoutput.pdf : pdf result file for Florida.R code pratical
   - Floridaoutput.tex : LaTex source codes to producing a pdf results file (Floridaoutput.pdf)

Author: Cherie Yu
Contact: cyy21@ic.ac.uk
