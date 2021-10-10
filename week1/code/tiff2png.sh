#!/bin/bash
#Author: cy221@ic.ac.uk
#Script: tiff2png.sh
#Description: converting all tiff files to png files 
#Arugments: f -> tiff filename 
#Date: Oct 2021

for f in *.tiff; #f is a variable that you identify as the file you want to convert
    do
        echo "Converting $f";  #You specified the variable therefore becoming $f (name of file.tiff)
        convert "$f"  "$(basename "$f" .tiff).png"; #Convert into a png, basename command extracts just the $f without the ending suffix
    done 

mv *.png ../results #need to add a star in front or else it won't work because loop was for all tiff conversion, therefore you have to specify this command to move ALL png

#exit