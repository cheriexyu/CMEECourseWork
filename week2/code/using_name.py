#!/usr/bin/env python3
#############################
#IMPORT TESTING WITH ANOTHER MODULE
#############################
# Filename: using_name.py

if __name__ == '__main__': 
    """import testing with a module"""
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

print("This module's name is: " + __name__)