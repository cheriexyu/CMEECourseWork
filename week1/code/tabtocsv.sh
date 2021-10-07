#!/bin/bash
#Author: cy221@ic.ac.uk
#Script: tabtocsv.sh
#Description: substitute the tabs in the files with commas
#
#Saves the output into a .csv file
#Arugments: 1 -> tab delimited file
#Date: Oct 2021

echo "Creating a comma delimited version of $1 ..." 
cat $1 | tr -s "\t" "," >> $1.csv #Within a new file called $1.csv, Write down $1, then transform and remove "\t" and ","
echo "Done!"
#exit

#In terminal code "echo -e "test \t\t test" >> NEW FILE"
#Output = test , test

#What does tr -s "\t" "," mean? Because its to remove space or subsitute?