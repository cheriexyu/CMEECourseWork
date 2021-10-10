#!/bin/bash
#Author: cy221@ic.ac.uk
#Script: MyExampleScript.sh
#Description: variable examples for shell scripts
#Arugments: msg1 -> Hello , msg2 -> UserName
#Date: Oct 2021

msg1="Hello"
msg2=$USER
echo "$msg1 $msg2" #Method one to print Hello $User (No need to specifiy $User as shown in computer system)
echo "Hello $USER" #Method two to print Hello $User
echo
#exit