x = [ i for i in range(10)]
print (x)

#SAME AS WRITING THE FOLLOWING LOOP

x = []
for i in range(10):
    x.append(i) #edit x with i = range 0 to 9 
print (x)



x = [i.lower() for i in ["LIST", "COMPREHENSIONS", "ARE", "COOL"]] #print out x list in lowercase
print (x)

#SAME AS WRITING THE FOLLOWING LOOP

x = ["LISTS", "COMPREHENSIONS", "ARE", "COOL"]
for i in range(len(x)): # explicit loop, for i in range 
    x [i] = x[i].lower()
print (x)

#SAME AS THIS IMPLICIT LOOP
x = ["LISTS", "COMPREHENSIONS", "ARE", "COOL"]
x_new = []
for i in x:
    x_new.append(i.lower())
print(x_new)

# Nested Loop
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened_matrix = []
for row in matrix:
    for n in row:
        flattened_matrix.append(n) #adds row (matrix) into flattened matrix
print(flattened_matrix)

# SAME AS THIS LIST COMPREHENSION
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened_matrix = [n for row in matrix for n in row] # for each row in the matrix make it into a single flattened row, same as above 
print(flattened_matrix)

#SETS AND DICTIONARY

words = (["These", "are", "some", "words"])
first_letters = set()
for w in words:
    first_letters.add(w[0]) #add() adds a given element to a set, 0 means the first letter
print(first_letters)

words = (["These", "are", "some", "words"])
first_letters = {w[0] for w in words} 
print(first_letters)

