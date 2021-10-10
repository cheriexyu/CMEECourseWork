#!/bin/bash
#Author: cy221@ic.ac.uk
#Script: CompileLaTeX.sh
#Description: compile LaTeX and bibliography into a pdf 
#Arugments: 1 -> LaTeX File
#Date: Oct 2021

if [ $# -eq 0 ]; then
    echo "No Input LaTex File Provided"
    exit 1
fi

FILE=$1
Var=$(basename "$FILE" | cut -d'.' -f1) #basename takes the filename and print out the last component of the filename or strip the end, cut based on the delimited . and print out the first field
echo "$Var" 
pdflatex $Var.tex #generates two files .log and .aux (and an incomplete .pdf)
bibtex $Var #reads .aux and produce two files .bbl and .blg, bibtex put citation into aux file
pdflatex $Var.tex #run updates on .log and .aux (writes in text on .aux)
pdflatex $Var.tex #updates .log and .aux and produce final .pdf
evince $Var.pdf& #opens pdf
mv $Var.pdf ../results

## Cleanup all extra files 
rm *.aux
rm *.log
rm *.bbl
rm *.blg

#.log only records how commands are runing