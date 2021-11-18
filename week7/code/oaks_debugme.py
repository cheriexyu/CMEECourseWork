#!/usr/bin/env python3
##################
#Practical Oaks Debugging with Doctests
##################
"""Practical debugging using doctests"""

import csv
import sys
import doctest

#write doctests to make sure that your is_an_oak function is working as expected (hint: >>> is_an_oak('Fagus sylvatica') should return False)
def is_an_oak(name):
    """Example doctests to show function is working as expected Find whether name is an oak
    >>> is_an_oak('Fagus sylvatica')
    False

    >>> is_an_oak('Pinus sylvestris')
    False

    >>> is_an_oak('quercus cerris')
    True

    >>> is_an_oak('Quercus cerris')
    True

    >>> is_an_oak('Crataegus monogyna')
    False

    >>> is_an_oak('Quercuss cerris')
    False

    """
    return name.lower().startswith('quercus ') #bug was here, spelling error 

def main(argv): 
    """writes a new csv file with just oak data"""
    """if it is an oak, print out string and write it in new csv file"""
    header = ['Genus','species']
    f = open('../data/TestOaksData.csv','r') #read the csv file
    taxa = csv.reader(f) # read f
    g = open('../data/JustOaksData.csv','w') #write a new csv file
    csvwrite = csv.writer(g) # write g
    csvwrite.writerow(header)
    oaks = set()
    #for b in taxa:
        #if b[0][0] in ("Genus"):
            #next(b)
        #else:
            #return(b)
            
    for row in taxa: # in f file
        """if f is an oak print out a statement"""
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0]+ " "):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])
        
    return 0
        
if (__name__ == "__main__"):
    """read main function"""
    status = main(sys.argv) #read the main function

doctest.testmod()
#starts off with reading the entire script from the top, then hits line 27, and go back up to main function