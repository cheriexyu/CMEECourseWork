#!/usr/bin/env python3
#############################
#LOOPS AND CONDITIONALS COMBINED
#############################

for j in range(12): #0 to 11
    if j % 3 == 0: #modulo operator e.g 8%3=2 , if J%3=0, true in this case 
        print('hello') #prints 4 times cause 4 numbers in range(12) has module of 0

for j in range(15):
    if j % 5 == 3: 
        print('hello') 
    elif j % 4 == 3: #in this case if range(15), print hello, elif=for else if, if the first condition for if is false, it checks the condition of elif
        print('hello')

# line 6 has 3 answers (3,8,13), line 8 has 3 answers (3,7,11) so hello should be print 6 times 
# HOWEVER, only 5 hellos are printed because the first condition is met already for 3 so 8th line wont be printed again, therefore only 5

z = 0 #LOOP, starts off with z is 0
while z != 15: # != not equal to , true statement 
    print('hello') 
    z = z + 3 # sub 0 into z first, then next z is 3 and go back to line 14, loop restarts until reaches z=15

z = 12
while z < 100: # true if z is smaller than 100
    if z == 31: # only one number which is 31
        for k in range(7): # range 0 to 6
            print('hello') # hello is print out 7 times [0,1,2,3,4,5,6]
    elif z == 18: # if above statement is false (if), the go to elif statement , only one number which is 18
        print('hello') # hello is print out 1 time
    z = z + 1 # if non above is true just jump to a new loop with a new z and not print out hello 
    # final is 8 output of hello


