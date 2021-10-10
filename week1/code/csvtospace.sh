#!/bin/bash
#Author: cy221@ic.ac.uk
#Script: boilerplate.sh
#Description: Converts CSV file to space seperated value version without changing the input file
#Arugments: 1 -> CSV file , 2 -> New Output file 
#Date: Oct 2021

if [ $# -le 1 ]; then #if command to make sure input files are provided: CSV + output filename 
    echo "No Input File Provided"
    exit 1
fi

echo "Creating a space seperated value version of $1"
cat $1 | tr -s "," " " >> $2 #subsituting all comma with one space value
echo "Done!"

mv $2 ../results

#exit
