
def modify_list_1(some_list): #new function
    print('got', some_list) #some_list is not definied so not printed
    some_list = [1, 2, 3, 4]
    print('set to', some_list) #WHY DOES NOTHING COME OUT FROM THIS PRINT 

my_list = [1,2,3]
print('before, my_list =', my_list)

modify_list_1(my_list) #print the top function ith my list 
#this function replaces the inside variable with my_list(1,2,3)
#loop backs to the top function and goes down the lines
#replaces print('got', my_list) due to the new variable 
#since some list is redifined again on like 4, it doesnt change on the line after

print('after, my_list =', my_list) #my list still stays the same even though it changed in the function

#FUNCTION WITH RETURN DIRECTIVE to RETURN THE VALUE OF THE INPUT LIST
def modify_list_2(some_list):
    print('got', some_list)
    some_list = [1,2,3,4]
    print('set to', some_list)
    return some_list #explicitly replaces some_list with all 1,2,3,4 and even outside of the function

my_list = modify_list_2(my_list)

print('after, my_list =', my_list) #this my_list has changed because we explicitly replaced it by return statement

#MODIFYING ORIGINAL LIST IN PLACE BY APPEND
def modify_list_3(some_list):
    print('got', some_list) # some list = 1,2,3
    some_list.append(4) # an actual modification of the list, adds 4 into a some list
    print('changed to', some_list) # some list =1,2,3,4, then jumps to line 41

my_list = [1,2,3]

print('before, my_list =', my_list)

modify_list_3(my_list)

print('after, my_list =', my_list) # new list is 1,2,3,4

#append can change original list object HOWEVER should still use return statement at the end of the function to be safe and 
#capture the output so it explicitly replaces the old variable.