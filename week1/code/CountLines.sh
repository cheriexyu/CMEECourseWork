#!/bin/bash
#Author: cy221@ic.ac.uk
#Script: CountLines.sh
#Description: use of variables to count lines for shell scripts
#Arugments: 1 -> Input File for counting 
#Date: Oct 2021

NumLines=`wc -l < $1` 
#Variable 'NumLines' mean count line number of $1, < redirects the content of the files into the command wc -l
#Without < it will also print out the script name
echo "The file $1 has $NumLines lines"
echo
#exit

#You need to specify what $1 since you need to count lines of a file, therefore in terminal you need to read zsh countlines.sh FILENAME
