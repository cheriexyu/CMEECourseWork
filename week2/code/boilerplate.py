#!/usr/bin/env python3
#Author: cy221@ic.ac.uk
#Script: boilerplate2.sh
#Description: simple boilerplate for python3
#Arugments: none
#Date: Oct 2021

"""Description of this program or application. 
You can use several lines""" #Docstring

#Internal variables signalled by __, special variables reserved for python
_appname_= '[python3]'
_author_= 'Cherie Yu (cy221@ic.ac.uk)'
_version_= '3.9.7'
_license_= "License for this code/program"

## imports ##
import sys #module to interface our program with the operating system

## constants ##

## functions ##
def main(argv): #defintions, start of a function, main means the main function, argv is the arguments from the bottom function
        """ Main entry point of the program """
        print('This is a boilerplate') # NOTE: indented using two tabs or 4 spaces
        return 0

if __name__ == "__main__": #adding this directs the python reader to set the special _name_ variable 
#to have a value called main. So the file will be usable as a script and an importable module (for usibility and packaging). 
#read my notes
    """Makes sure the "main" function is called from command line"""  
    status = main(sys.argv) #argv = argument variable, an objected created using the sys module that contains the names of the argument variables in the current script
    sys.exit(status) #Way to terminate the program in an explicit manner
    #arguments from here is fed back to the main function



