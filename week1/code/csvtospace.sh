#!/bin/bash
#Description: Converts CSV to SSV named files

for f in *.csv;
    do  
        echo "Creating a space seperated value version of $f;
        convert "$f"  "$(basename "$f" .csv).SSV";
    done 

