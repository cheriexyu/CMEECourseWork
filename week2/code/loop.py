#!/usr/bin/env python3
#############################
# FOR loops in Python
#############################

for i in range(5):
    print(i)

my_list = [0, 2, "geronimo", 3.0, True, False]
for k in my_list: #naming k as a variable and subing it with my_list 
    print(k) 

total = 0 
summands = [0, 1, 11, 111, 1111]
for s in summands:
    total = total + s #this loop continues on and replaces the previous loop total with the new total 
    print(total)

# WHILE loops in python
z = 0
while z < 100:
    z = z + 1 #prints out all the numbers to 100, this loop replaces the last z with the new z 
    print(z)

b = True #True keeps printing
while b:
        print("GERONIMO! infinite loop! ctrl+c to stop!")
# ctrl + c to stop!