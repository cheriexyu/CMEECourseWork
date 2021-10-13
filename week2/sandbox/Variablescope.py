#################
#Local variables and global variables
################
#Local variables and explicitly returning function to show inside and outside function

_a_global = 10 #global variable

if _a_global >= 5: #global variable, if a_global is equal or bigger than 5, go to this loop
    _b_global = _a_global + 5

def a_function(): # Defining a new function
    _a_global = 5 # local variable, we overwritten a_global with 5 instead of 10 but it stayed inside this function

    if _a_global >= 5: # if a is bigger or equal to 5 which it is
        _b_global = _a_global + 5 # b = 10
    
    _a_local = 4 

    print("Inside the function, the value of _a_global is ", _a_global) #prints 5
    print("Inside the function, the value of _b_global is ", _b_global) #prints 10
    print("Inside the function, the value of _a_local is ", _a_local) #prints 4
    
    return None # good practice to add this just like adding exit in bash. 

a_function() # explicitly return the function to make it visible outside function, prints out the function which is the three line inside the function

print("Outside the function, the value of _a_global is ", _a_global) # prints 10 from first if statement
print("Outside the function, the value of _b_global is ", _b_global) # prints 15 from the first if statements

#BUT if you assign a variable outside the function, it will still be available inside the function, not the other way around

#################
#Global Variables
#################

_a_global = 10

print("Outside the function, the value of _a_global is", _a_global) # a global = 10

def a_function():
    global _a_global #global variable from inside a function 
    _a_global = 5
    _a_local = 4
    
    print("Inside the function, the value of _a_global is ", _a_global) # a global = 5
    print("Inside the function, the value _a_local is ", _a_local) # a local = 4
    
    return None

a_function() # print the above two lines (print)

print("Outside the function, the value of _a_global now is", _a_global) # a global = 5 , the a is replaced/overwritten by the global value inside the function

#Global variables can also be Inside Nested Functions
def a_function():
    _a_global = 10

    def _a_function2():
        global _a_global
        _a_global = 20 # global keyword inside the inner function resulted in change of value in a global to 20 but only outside of the scope of the function
    
    print("Before calling a_function, value of _a_global is ", _a_global) # still 10

    _a_function2()
    
    print("After calling _a_function2, value of _a_global is ", _a_global) # still 10
    
    return None

a_function()

print("The value of a_global in main workspace / namespace is ", _a_global) # a global is the global variable 20 
# within the scrope of a function, the value of a still remained at 10 but only in the outside function is when the a global has changed due to line 59

#Example 2 
_a_global = 10 # The main difference from the one above , defined in advanced

def a_function():

    def _a_function2():
        global _a_global
        _a_global = 20
    
    print("Before calling a_function, value of _a_global is ", _a_global) # a is 10

    _a_function2()
    
    print("After calling _a_function2, value of _a_global is ", _a_global) # a is 20 WHY IS THIS @) 

a_function()

print("The value of a_global in main workspace / namespace is ", _a_global) # a is 20