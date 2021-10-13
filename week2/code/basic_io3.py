#############################
# STORING OBJECTS
#############################
# To save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11} #set a new variable
print(my_dictionary)

import pickle 

f = open('../sandbox/testp.p','wb') #w tells to open a file for writing, b tells to accept binary files 
pickle.dump(my_dictionary, f) #using pickled save my dictionary into f (testp.p)

f.close()

## Load the data again
f= open('../sandbox/testp.p','rb') #opening back file
another_dictionary = pickle.load(f) #open pack f into a human readable file 
f.close()

print(another_dictionary)
