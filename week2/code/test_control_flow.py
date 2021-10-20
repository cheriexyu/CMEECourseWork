#!/usr/bin/env python3
##################
#Control Flow Debugging with DocTest
##################

"""Description of this program or application. 
You can use several lines""" #Docstring

"""Some functions exemplifying the use of control statements"""
#docstrings are considered part of the running code (normal comments are
#stripped). Hence, you can access your docstrings at run time.
__author__ = 'Cherie Yu (cy221@ic.ac.uk)'
__version__ = '0.0.1'

## imports ##
import sys #module to interface our program with the operating system
import doctest #Import the doctest module

## functions ##

def even_or_odd(x=0): # if not specified, x should take value 0.
    """Find whether a number x is even or odd.

    >>> even_or_odd(10)
    '10 is Even!'

    >>> even_or_odd(5)
    '5 is Odd!'

    whenever a float is provided, then the closest integer is used:
    >>> even_or_odd(3.2)
    '3 is Odd!'

    in case of negative numbers, the positive is taken:
    >>> even_or_odd(-2)
    '-2 is Even!'

    """
    #Define funtion to be tested
    if x % 2 == 0: #The conditional if 
        return "%d is Even!" % x # % x at the end is used to tell %d, a placeholder what it is and to sub
    return "%d is Odd!" % x

#def main(argv):  # Step 2
    print(t.even_or_odd(22)) # Loop 1 to the top
    print(t.even_or_odd(33)) # Loop 2 to the top 
    return 0

#if (__name__ == "__main__"): # Step 1
    status = main(sys.argv) 

doctest.testmod() #To run with embedded tests

