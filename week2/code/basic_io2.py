#!/usr/bin/env python3
#############################
# FILE INPUT
#############################
# Save the elements of a list to a file 
list_to_save = range(100)

f = open('../sandbox/testout.txt','w') # w tells to open a file for writing
for i in list_to_save:
    """add a new line at the end of file f"""
    f.write(str(i) + '\n') #add a new line at the end

f.close()
