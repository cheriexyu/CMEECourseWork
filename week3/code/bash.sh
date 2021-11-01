#!/bin/bash
pdflatex $1.tex
pdflatex $1.tex

## Cleanup
rm *.aux
rm *.log
rm *.bbl
rm *.blg
