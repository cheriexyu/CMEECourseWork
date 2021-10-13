## Finds just those taxa that are oak trees from a list of species

taxa = [ 'Quercus robur',
         'Fraxinus excelsior',
         'Pinus sylvestris',
         'Quercus cerris',
         'Quercus petraea',
       ]

def is_an_oak(name): # a function = true or falste statement, define is_an_oak, replace name with the name of the taxa
    return name.lower().startswith('quercus') #make name lower case and if starts with quercus = TRUE (it is an oak)

##Using for loops to make a set
oaks_loops = set() #new set called oaks_loops
for species in taxa: 
    if is_an_oak(species): #if it is an oak species like from above function
        oaks_loops.add(species) #add it into the set called oak loop
print(oaks_loops) #gets a set of oak tree 

##Using list comprehensions
oaks_lc = set([species for species in taxa if is_an_oak(species)]) #list compregension method for above loop 
print(oaks_lc)

##Get names in UPPER CASE using for loops
oaks_loops = set() 
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species.upper()) #add it into oaks_loops in uppercase
print(oaks_loops)

##Get names in UPPER CASE using list comprehensions
oaks_lc = set([species.upper() for species in taxa if is_an_oak(species)]) #Comprehension form of the above loop. uppercase first in the bracket 
print(oaks_lc) 