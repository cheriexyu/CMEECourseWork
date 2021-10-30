#!/usr/bin/env python3
#############################
# FOR loops in Python
#############################
"""Loops in Python"""

for i in range(5):
    """print the range from 1 to 5"""
    print(i)

my_list = [0, 2, "geronimo", 3.0, True, False]
"""loops using variables"""
for k in my_list: #naming k as a variable and subing it with my_list 
    print(k) 

total = 0 
summands = [0, 1, 11, 111, 1111]
for s in summands:
    """loops on and replace the previous total with a new total"""
    total = total + s #this loop continues on and replaces the previous loop total with the new total 
    print(total)

# WHILE loops in python
z = 0
while z < 100:
    """While loops keeps looping until reaches a condition if z less than 100"""
    """loops over and replaces previous z with the new z"""
    z = z + 1 #prints out all the numbers to 100, this loop replaces the last z with the new z 
    print(z)

b = True #True keeps printing
while b:
    """Infinite while loop"""
        print("GERONIMO! infinite loop! ctrl+c to stop!")
# ctrl + c to stop!