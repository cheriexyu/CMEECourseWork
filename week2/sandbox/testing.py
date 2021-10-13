x = 11

for i in range(x):
    if i > 3: 
        print(i)

for i in range(10):
    print(i)

a = range(10)
a

for i in range(1,6):
    print(i)

for i in range(2,10,2): #skip odd numbers
    print(i)

for i in range(2,10,3): #skips 3 numbers starting from 2 (2,5,8)
    print(i)

for i in range(2,10,4): #skips 4 number starting from 2 (2,6)
    print(i)

my_iterable = [1,2,3]
type(my_iterable)

my_iterable = iter(my_iterable)
type(my_iterable)

next(my_iterable)

#Delineate a Function, saving foo in a memory as the mutiply operation
def foo(x):
    x *= x #same as x=x*x (multiply)
    print (x)
    return x #need this to caputure and stores foo
foo(2)
foo(5)

y = foo(2)
y
type(y)

def foo(x):
    x *= x #same as x=x*x (multiply)
    print (x)
    #return x does not capture or store if missing

y = foo(2)








    