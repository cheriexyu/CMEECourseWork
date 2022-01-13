#!/usr/bin/env python3
#############################
# Profiling in Python, more efficent method 
#############################
"""Profiling code to find the speed at each sections, with faster alterations to code compared to profileme.py"""
"""halved the running time"""

def my_squares(iters):
    """changed append loop to a list comprehension"""
    out = [i**2 for i in range (iters)] #list comprehension, didnt write append compared to profilem.pys
    return out

def my_join(iters,string):
    """concatenate iters and string using '+' command"""
    out = ''
    for i in range(iters):
        out += "," + string #elimate jqoin. for string with explicit string concatenate (+=) adds another value into the assigned value of the variable, add into out
    return out

def run_my_funcs(x,y):
    """run functions of the above"""
    print(x,y)
    my_squares(x) 
    my_join(x,y)
    return 0

run_my_funcs(10000000,"My string")
