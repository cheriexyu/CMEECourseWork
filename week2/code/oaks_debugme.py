import csv
import sys

#Define function
def is_an_oak(name):
    #import ipdb; ipdb.set_trace()
    """ Returns True if name is starts with 'quercus' """
    """Will return False if it is not an oak"""
    return name.lower().startswith('quercus') #bug was here, spelling error 

def main(argv): 
    """writes a new csv file with just oak data"""
    """if it is an oak, print out string and write it in new csv file"""
    f = open('../data/TestOaksData.csv','r') #read the csv file
    g = open('../data/JustOaksData.csv','w') #write a new csv file
    taxa = csv.reader(f) # read f
    csvwrite = csv.writer(g) # write g
    oaks = set()
    for row in taxa: # in f file
        #import ipdb; ipdb.set_trace()
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])
        
    return 0
    
if (__name__ == "__main__"): 
    status = main(sys.argv) #read the main function


#starts off with reading the entire script from the top, then hits line 27, and go back up to main function