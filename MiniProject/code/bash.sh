#!/bin/bash

pdflatex Report.tex #generates two files .log and .aux (and an incomplete .pdf)
bibtex Report #reads .aux and produce two files .bbl and .blg, bibtex put citation into aux file
pdflatex Report.tex #run updates on .log and .aux (writes in text on .aux)
pdflatex Report.tex #updates .log and .aux and produce final .pdf
evince Report.pdf & #opens pdf

## Cleanup
rm *.aux
rm *.log
rm *.bbl
rm *.blg
