#!/bin/bash
#Author: cy221@ic.ac.uk
#Script: tabtocsv.sh
#Description: substitute the tabs in the files with commas
#Arguments: 1 -> tab delimited file
#Date: Oct 2021

if [ $# -eq 0 ]; then
    echo "No Input File Provided"
    exit 1
fi

echo "Creating a comma delimited version of $1 ..." 
cat $1 | tr -s "\t" "," >> $1.csv #Within a new file called $1.csv, Write down $1, then transform and remove "\t" and ","
mv $1.csv ../results
echo "Done!"
#exit

#In terminal code "echo -e "test \t\t test" >> NEW FILE"
#Output = test , testt
#tr -s [string1] [string2], subsitute many of string 1 with one of string 2 
