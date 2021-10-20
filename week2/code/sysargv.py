#!/usr/bin/env python3
#############################
#RUNNING SYS.ARGV OBJECTS
#############################
import sys
print("This is the name of the script:", sys.argv[0]) #filename is [0]
print("Number of arguments:", len(sys.argv))
print("The arguments are:", str(sys.argv))

#First list of the sys.argv is always filename 