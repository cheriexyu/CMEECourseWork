#!/usr/bin/env python3
#############################
# HANDLING CSV's
#############################
# To manipulate CSV files
import csv

# Read a file containing:
# 'Species','Infraorder','Family','Distribution','Body mass male (Kg)'
with open('../data/testcsv.csv','r') as f:

    csvread = csv.reader(f) 
    temp = [] #you make a empty list and set is as the object temp
    for row in csvread: 
        temp.append(tuple(row)) #changing temp list with tuple(list) of rows, you are locking the rows together as a immendible set
        print(row)

# write a file named bodymass.csv containing only species name and Body mass
with open('../data/testcsv.csv','r') as f:
    with open('../data/bodymass.csv','w') as g:

        csvread = csv.reader(f) #open file f and make it as an object
        csvwrite = csv.writer(g) #writing a file g.csv and make it as an object
        for row in csvread: 
            print(row) 
            csvwrite.writerow([row[0], row[4]]) #write the rows in the objects in csvwrite aka g object
