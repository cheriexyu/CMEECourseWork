#############################
# FILE INPUT
#############################
# Open a file for reading 
with open('../sandbox/test.txt', 'r') as f: #r = opens a file for reading, example of opening files with 'with'
# use "implicit" for loop:
# Command to print out the lines in to text, if the object is a file, python will cycle over lines
    for line in f: 
        print(line)

# close the file
f.close()

# Same example, skip blank lines
f = open('../sandbox/test.txt', 'r')
for line in f:
    if len(line.strip()) > 0: #checks if the line is empty
        print(line)

f.close()


