#!/usr/bin/env python3
#############################
# Profiling in Python
#############################
"""Profiling code to find the speed at each sections"""

def my_squares(iters):
    """append the output of range(iters) to the power of 2 into a list"""
    out=[]
    for i in range(iters):
        out.append(i**2)
    return out 

def my_join(iters,string):
    """concatenate string and iters to the out output using join command"""
    out=''
    for i in range(iters):
        out += string.join(",")
    return out

def run_my_funcs(x,y):
    """run the functions listed above"""
    print(x,y)
    my_squares(x)
    my_join(x,y)
    return 0

run_my_funcs(10000000,"My string")