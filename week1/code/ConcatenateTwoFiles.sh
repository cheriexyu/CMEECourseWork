#!/bin/bash

cat $1 > $3 #Write $1 in $3
cat $2 >> $3 #Write $2 in the second line of $3
echo "Merged File is" #First line in terminal with the string "Merged File is"
cat $3 #Show file text of $3

#Combining and merging two files together, When zsh in terminal need to write 4 subsitutes e.g zsh ConcatenateTwoFiles.sh FILE1($1) FILE2($2) $3.txt