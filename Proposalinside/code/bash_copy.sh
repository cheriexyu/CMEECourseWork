#!/bin/bash

pdflatex project_proposal.tex #generates two files .log and .aux (and an incomplete .pdf)
bibtex project_proposal #reads .aux and produce two files .bbl and .blg, bibtex put citation into aux file
pdflatex project_proposal.tex #run updates on .log and .aux (writes in text on .aux)
pdflatex project_proposal.tex #updates .log and .aux and produce final .pdf

## Cleanup
rm *.aux
rm *.log
rm *.bbl
rm *.blg

mv project_proposal.pdf ../results/
