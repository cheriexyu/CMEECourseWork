# *Week 1*


## General Description

In week 1, we underwent practical exercises using UNIX systems to create working bash scripts.

***

## Languages
Unix Shell and Bash Script

***
## Dependencies
imagemagick, LaTeX

***
## Installation

Use the package manager [homebrew](https://brew.sh/) to install imagemagick and LaTeX.

```bash
brew install imagemagick
```

```bash
brew install --cask MacTeX 
```

To run bash scripts on Terminal:

```bash
bash script.sh
```

Some scripts require one or more input files and will be instructed when attempting to run bash scripts. 

***
## Project Structure and Usage

../code

   - UnixPrac1.txt : Unix shell exercise with ../data/fasta FASTA files
   - boilerplate.sh : Simple boilerplate for shell scripts 
   - tabtocsv.sh : Bash script to substitue tabs with commas in files
   - CountLines.sh : Bash script to countlines in files
   - ConcatenateTwoFiles.sh : Bash script to merge two files to a new output
   - tiff2png.sh : Bash script to convert .tiff to .png with imagemagick
   - csvtospace.sh : Bash script to take .CSV and convert to space separated value files in a new output 
   - variables.sh : Show how to use variables in shell scripts
   - MyExampleScript.sh : Introduces how to use the $USER (same as $USERNAME) environmental variable
   - CompileLaTeX.sh : Bash script to compile a LaTeX .pdf document 
   - FirstExample.tex : An example LaTex docuemnts 
   - FirstBiblio.bib : Biblbiography for the LaTex file FirstExample.tex

../data

   - spawannxs.txt : List of protected species of Marine and Coastal Flora 
   - ../data/Fasta : Directory containing fasta files of sequence data
   - ../data/Temperature : Directory containing csv Temperature files 

../results

../sandbox

Author: Cherie Yu

Contact: cyy21@ic.ac.uk
