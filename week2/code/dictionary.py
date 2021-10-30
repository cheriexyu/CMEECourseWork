#!/usr/bin/env python3
##################
#Practical Comprehensions using Dictionary
##################

taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa.
# 
# An example output is:
#  
# 'Chiroptera' : set(['Myotis lucifugus']) ... etc.
#  OR,
# 'Chiroptera': {'Myotis lucifugus'} ... etc

#Chiroptera, Carnivora, Afrosoricida, Rodentia
#{} creates an empty dictionary

newlist = {} #When you do dictionary {} means that already
for spp, fam in taxa: # for x,y in the list
    """create a new dictionary listing out all species within each families"""
    newlist.setdefault(fam, []).append(spp) #setdefault() searches for a key and displays the value. 
    #but if that value is not present, it will create a new key
    #It loops through taxa, gets the first one, takes fam = y puts it in the front, and then puts species into []
    #without append spp, the [] will be blank 
    #put nothing inside [] to show no key, so the value in spp will become that new value
    #dictioinary prevents repeating as well so the same family won't be repeated 
print(newlist)

