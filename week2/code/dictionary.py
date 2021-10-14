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

#Rodentia
rodent = []
for a in taxa:
        if a[1]=="Rodentia":
                rodent.append(a)
print(rodent)



rodentdict={}
rodentdict['Rodentia'] = []
rodentdict['Rodentia'].append(rodent[0])
print (rodentdict) 

###

# Get list of Families
# for each family:
    # Make list of spp


fams = set([])
for t in taxa:
        fams.add(t[1])
fams = list(fams)

final_dict = {}
for fam in fams:
        tmp_list = []
        for t in taxa:
                if t[1] == fam:
                        tmp_list.append(t[0])
        final_dict[fam] = set(tmp_list)

print(final_dict)

taxa_dic = {        :}{          }

