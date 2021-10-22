#!/usr/bin/env python3
#############################
#CONTROL FLOW
#############################

"""Some functions exemplifying the use of control statements""" #Docstring
#docstrings are considered part of the running code (normal comments are
#stripped). Hence, you can access your docstrings at run time.
__author__ = 'Cherie Yu (cy221@ic.ac.uk)'
__version__ = '0.0.1'

## imports ##
import sys #module to interface our program with the operating system

## functions ##

def even_or_odd(x=0): # if not specified, x should take value 0.
   
    """Find whether a number x is even or odd."""
    if x % 2 == 0: #The conditional if 
        return "%d is Even!" % x # % x at the end is used to tell %d, a placeholder what it is and to sub
    return "%d is Odd!" % x

def largest_divisor_five(x=120): # if z is not specified , x will be 120 
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
    else: # When all other (if,elif) conditions are not met
        return "No divisor found for %d!" % x # Each function can return a value or a variable
    return "The largest divisor of %d is %d" % (x,largest)

def is_prime(x=70):
    """Find whether an integer is prime."""
    for i in range(2,x): # "range" returns a squence of integers
        if x % i == 0:
            print("%d is not a prime: %d is a divisor" % (x,i))
            return False
    print("%d is a prime!" % x)
    return True 

def find_all_primes(x=22):
    """Find all the primes up to x"""
    allprimes = []
    for i in range(2, x + 1):
        if is_prime(i):
            allprimes.append(i)
    print("There are %d primes between 2 and %d" % (len(allprimes), x))
    return allprimes

def main(argv):  # Step 2
    print(even_or_odd(22)) # Loop 1 to the top
    print(even_or_odd(33)) # Loop 2 to the top 
    print(largest_divisor_five(120)) # Loop3 to the top
    print(largest_divisor_five(121)) #Loop 4
    print(is_prime(60)) #Loop 5
    print(is_prime(59)) #Loop 6
    print(find_all_primes(100)) #Loop 7
    return 0

if (__name__ == "__main__"): # Step 1
    status = main(sys.argv) 
    sys.exit(status) 





