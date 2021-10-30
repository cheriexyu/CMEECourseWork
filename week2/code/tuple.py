#!/usr/bin/env python3
##################
#Practical Comprehensions using tuples
##################

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
        )

# Birds is a tuple of tuples of length three: latin name, common name, mass.
# write a (short) script to print these on a separate line or output block by species 
# 
# A nice example output is:
# 
# Latin name: Passerculus sandwichensis
# Common name: Savannah sparrow
# Mass: 18.7
# ... etc.

# Hints: use the "print" command! You can use list comprehensions!

sparrow=[b for b in birds[0]]
"""In the first tupple, list out the latin name, common name, mass"""
print ("Latin name:" + sparrow[0] )
print ("Common name:" + sparrow[1])
print ("Mass:" + str(sparrow[2])) #need to convert the mass into a string, or change plus sign into comma 

martin=[c for c in birds[1]]
"""In the second tupple, list out the latin name, common name, mass"""
print ("Latin name:" + martin[0] )
print ("Common name:" + martin[1])
print ("Mass:" + str(martin[2])) 

yellow=[d for d in birds[2]]
"""In the third tupple, list out the latin name, common name, mass"""
print ("Latin name:" + yellow[0] )
print ("Common name:" + yellow[1])
print ("Mass:" + str(yellow[2])) 

dark=[e for e in birds[3]]
"""In the forth tupple, list out the latin name, common name, mass"""
print ("Latin name:" + dark[0] )
print ("Common name:" + dark[1])
print ("Mass:" + str(dark[2])) 

swallow=[f for f in birds[4]]
"""In the last tupple, list out the latin name, common name, mass"""
print ("Latin name:" + swallow[0] )
print ("Common name:" + swallow[1])
print ("Mass:" + str(swallow[2])) 