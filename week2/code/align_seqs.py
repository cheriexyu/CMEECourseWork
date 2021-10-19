#!/usr/bin/env python3

"""Python program that aligns two DNA sequences and calculates the best alignment score"""

__appname__ = '[application name here]'
__author__ = 'Your Name (your@email.address)'
__version__ = '0.0.1'
__license__ = "License for this code/program"

## Imports ##
import sys # module to interface our program with the operating system

# Import input code file 
with open('../data/testalign.txt', 'r') as f:
    """Opening input file and assigning variables to each sequence"""
    lines = []
    for line in f:
        lines.append(line.strip())
    print(lines)
    
seq1 = lines[0]
seq2 = lines[1]
print(seq1)
print(seq2)

# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

## Functions ##
def main(argv):
    """ Main entry point of the program """
    print('This is the best alignment score between the two sequences') # NOTE: indented using two tabs or 4 spaces
    return 0

#Positioning the longer sequence on top
l1 = len(seq1) # Count the length of the sequences, In this example, l2 is longer than l1
l2 = len(seq2)
print(l1) #10
print(l2) #16
if l1 >= l2: # if l1 is longer than l2
    s1 = seq1 #longer sequence
    s2 = seq2 #shorter sequence
else:
    s1 = seq2 #16
    s2 = seq1 #10
    print(s1) 
    print(s2)
    l1, l2 = l2, l1 # swap the two lengths
print(l1)
print(l2)
print(s1) # equals to seq2
print(s2) # equals to seq1

# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    """calculate alignment score"""
    matched = "" # to hold string displaying alignements
    score = 0 
    for i in range(l2): #Starting from base 0 to base 9, l2 is the shorter sequence e.g 10, 
        #import ipdb; ipdb.set_trace()
        if (i + startpoint) < l1: # If the end of the sequence hasnt been reached, then starting from the startpoint + i (rangel2), count the number of bases
            if s1[i + startpoint] == s2[i]: # if the bases match 
                matched = matched + "*" # add a star to the  matched 
                score = score + 1 # and add a score point 
            else:
                matched = matched + "-" #if the bases don't matched 

    # some formatted output
    print("." * startpoint + matched) #print out matched score (- and *) 
    # "." is saying to multiply with the number of startpoint to start e.g startpoint = 0, multiplt "."" x 0 = 0 so start the signs at the beginning  
    print("." * startpoint + s2) #print out the s2 from the startpoint, just like the above
    print(s1) #longer sequenece
    print(score) 
    print(" ")

    return score #end the code with a score 

# Test the function with some example starting points:
calculate_score(s1, s2, l1, l2, 0)
calculate_score(s1, s2, l1, l2, 1) # code starts on the 2nd
calculate_score(s1, s2, l1, l2, 5) # code starts on the 6th

# now try to find the best match (highest score) for the two sequences, find the sequence with the highest alignment 
my_best_align = None #null value or no value 
my_best_score = -1 #why -1 because best score can be 0

for i in range(l1): # Note that you just take the last alignment with the highest score, l1 = 16
    """Calculate the highest alignment score"""
    #import ipdb; ipdb.set_trace()
    z = calculate_score(s1, s2, l1, l2, i) #the score of alignment from above function
    if z > my_best_score: #if alignment score is higher than the best score 
        my_best_align = "." * i + s2 # think about what this is doing!
        # "." multiplied by the starting point + shorter sequence
        my_best_score = z # best score = calculated score per i in range, as it the short sequence moves one base to the right acording to the longer sequence
print(my_best_align) #the best alignment which is in startingpoint 0
print(s1) #the longer sequence
print("Best score:", my_best_score)

##File Output##
lines=[my_best_align, s1, "Best score:"+ str(my_best_score)]
with open('../results/best_alignment.txt', 'w' ) as b: 
    for line in lines:
        b.write(line)
        b.write('\n')
print("Best alignment saved to result folder")

# it shows the highest best score because it goes from z = calculated score then if z > my_best_score will replace the best score 
#and when it loops it keeps changing my best score with the largest value (line 63 and 66)
if __name__ == "__main__": 
    """Makes sure the "main" function is called from command line"""  
    status = main(sys.argv)
    sys.exit(status)