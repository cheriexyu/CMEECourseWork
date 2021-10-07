#!/bin/bash

for f in *.tiff; #f is a variable that you identify as the file you want to convert
    do
        echo "Converting $f";  #You specified the variable therefore becoming $f (name of file.tiff)
        convert "$f"  "$(basename "$f" .tiff).png"; #Convert into a png, basename command extracts just the $f without the ending suffix
    done 

