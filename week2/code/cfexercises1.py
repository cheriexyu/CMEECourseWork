#!/usr/bin/env python3
#############################
# USE OF CONDITIONALS IN FUNCTIONS
#############################
"""Use of conditionals in loop functions"""

## imports ##
import sys 
import doctest

## functions ##

def foo_1(x): 
    """Takes in x and returns x to the power of 0.5""" #Docstring
    return x ** 0.5 #for foo_1, return x a power of 0.5

def foo_2(x,y):
    """Compares x and y, and print out x or y depending on which is bigger"""
    if x > y: 
        return x #if x is bigger than y, print out x and leave command
    return y #if y is bigger, print out y and leave command
#RETURN= An exit command, if the condition is met, it will jump out of the function without touching the bottom commands unlike print

def foo_3(x,y,z): #Switching places of numbers
    """if x is bigger than y, switch the places of x and y using a placeholder""" 
    """if y is bigger than z, switch the places of y and z using a placeholder"""
    if x > y: 
        tmp = y #temporary placeholder file to store y value
        y = x # y is now the x value
        x = tmp #x is now the value in the tmp placeholder 
    if y > z:
        tmp = z #z value is in the temporary placehold
        z = y #z is y value
        y = tmp #y is the value in the temporary placeholder
    return [x,y,z]

def foo_4(x):
    """Using the values between the range 1 to x+1, function loops between each value and replaces the result of the previous loop"""
    """keeps looping until it reaches the end value"""
    result = 1
    for i in range(1, x + 1): 
        result = result * i #keeps looping until it reached x+1, and replaces the result of the previous loop
        print(result)
    return result

def foo_5(x): # a recursive (calls itself) function that calculates the factorial of x
    """ if x is 1, return the output as 1"""
    """ if x is not 1, then produce a factorial of x and return""" 
    if x == 1:  #if x = 1 return 1
        return 1
    return x * foo_5(x-1) #equation to produce a factorial of x 
#factorial e.g 5! = 5x4x3x2x1 

def foo_6(x): # Calculate the factorial of x in a different way
    """while x is bigger than 1 then """
    """if x is less than 0, undergo command and replace x with a new value and repeats the loop"""
    facto = 1
    while x >= 1: #while statements execute a set of command as long as the condition is true 
        facto = facto * x 
        x = x - 1
        print(x)
    return facto 

def main(argv):  # Step 2
    """Testing functions with assigned variables"""
    print(foo_1(11)) # Loop 1 to the top
    print(foo_1(9)) # Loop 2 to the top 
    print(foo_2(4,3)) # Loop3 to the top
    print(foo_2(5,8)) #Loop 4
    print(foo_3(4,3,2)) #Loop 5
    print(foo_3(1,5,4)) 
    print(foo_4(5)) #Loop 6
    print(foo_5(10)) #Loop 7
    return 0

if (__name__ == "__main__"): # Step 1
    status = main(sys.argv) 
    sys.exit(status) 

doctest.testmod() 

