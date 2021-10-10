#!/bin/bash
#Author: cy221@ic.ac.uk
#Script: variables.sh
#Description: Assigning and use of variables for shell scripts
#Arugments: MyVar -> 'string', a and b -> read number provided by reader
#Date: Oct 2021

#Shows the use of variables
MyVar='some string'
echo 'the current value of the variable is' $MyVar #You add dollar sign infront of variable to signify it is a variable 
echo 'Please enter a new string'
read MyVar #Tells audience to give a new string to MyVar and read that 
echo 'the current value of the variable is' $MyVar #Replaces the MyVar in line 4 with the new one from line 7

## Reading multiple values
echo 'Enter two numbers separated by space (s)'
read a b #Tells audience to put a string for a and b, and shell to read it as that
echo 'you entered' $a 'and' $b '. Their sum is:' #Dollar sign means signify it as variable
mysum=`expr $a + $b` #Adding two numbers in Bash and putting it as a variable
echo $mysum

#exit