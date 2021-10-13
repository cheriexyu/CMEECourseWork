# What does each of foo_x do?

def foo_1(x): 
    return x ** 0.5 #for foo_1, return x a power of 0.5

def foo_2(x,y):
    if x > y: 
        return x #if x is bigger than y, print out x and leave command
    return y #if y is bigger, print out y and leave command

#RETURN= An exit command, if the condition is met, it will jump out of the function without touching the bottom commands unlike print

def test(x,y):
    if x > y:
        print x
    print y
#PRINT

def foo_3(x,y,z): #Switching places of numbers 
    if x > y: 
        tmp = y #temporary placeholder file to store y value
        y = x # y is now the x value
        x = tmp #x is now the value in the tmp placeholder 
    if y > z:
        tmp = z #z value is in the temporary placehold
        z = y #z is y value
        y = tmp #y is the value in the temporary placeholder
    return [x,y,z]

def foo_4(x):
    result = 1
    for i in range(1, x + 1): 
        result = result * i #keeps looping until it reached x+1, and replaces the result of the previous loop
        print(result)
    return result

def foo_5(x): # a recursive (calls itself) function that calculates the factorial of x
    if x == 1:  #if x = 1 return 1
        return 1
    return x * foo_5(x-1) #equation to produce a factorial of x 
#factorial e.g 5! = 5x4x3x2x1 

def foo_6(x): # Calculate the factorial of x in a different way
    facto = 1
    while x >= 1: #while statements execute a set of command as long as the condition is true 
        facto = facto * x 
        x = x - 1
        print(x)
    return facto 
