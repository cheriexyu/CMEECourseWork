#!/usr/bin/env python3
##################
#Debugging Funtion
##################
"""Testing how to debug a function"""

def buggyfunc(x):
    """using ipdb to debug this function"""
    y = x
    for i in range(x):
        try: #tries to do something and if it doesnt work (error) transfer control to the except block 
        #and whatever you ask python to do in that block get executed. 
        #use this if you want the program to give feedback in errors that are not common
            y = y-1
            z = x/y
        except:
            print(f"This didn't work; x = {x}; y = {y}")
        else:
            print(f"OK: x = {x}; y = {y}, z = {z};")
    return z

buggyfunc(20)

