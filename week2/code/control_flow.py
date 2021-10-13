#!/usr/bin/env python3
#Author: cy221@ic.ac.uk
#Script: boilerplate2.sh
#Description: simple boilerplate for python3
#Arugments: none
#Date: Oct 2021

"""Description of this program or application. 
You can use several lines""" #Docstring

"""Some functions exemplifying the use of control statements"""
#docstrings are considered part of the running code (normal comments are
#stripped). Hence, you can access your docstrings at run time.
__author__ = 'Cherie Yu (cy221@ic.ac.uk)'
__version__ = '0.0.1'

## imports ##
import sys #module to interface our program with the operating system

def even_or_odd(x=0) # if not specified, x should take value 0.
        
        """Find whether a number x is even or odd."""
        if x % 2 == 0: #The conditional if 
                return "%d is Even!" % x
        return "%d is Odd!" % x

def largest_divisor_five(x=120):
        """Find which is the largest divisor of x among 2,3,4,5."""
        largest = 0
        if x % 5 == 0:
                largest = 5
        elif x % 4 == 0: #means "else, if"
                largest = 4
        elif x % 3 == 0:
                largest = 3
        elif x % 2 == 0:
                largest = 2
        else: 
        


