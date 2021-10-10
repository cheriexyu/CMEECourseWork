#!/bin/bash
#Author: cy221@ic.ac.uk
#Script: ConcatenateTwoFiles.sh
#Description: combining two files into a new output file 
#Arugments: 1 -> Input File 1, 2 -> Input File 2, 3 -> New Output File 
#Date: Oct 2021

if [ $# -le 2 ]; then #-le means less or equal to 2 
    echo "Error, Need Input Files"
    exit 1
fi

cat $1 > $3 #Write $1 in $3
cat $2 >> $3 #Write $2 in the second line of $3
echo "Merged File is" #First line in terminal with the string "Merged File is"
cat $3 #Show file text of $3
mv $3 ../results

#exit

#Combining and merging two files together, When zsh in terminal need to write 4 subsitutes e.g zsh ConcatenateTwoFiles.sh FILE1($1) FILE2($2) $3.txt
