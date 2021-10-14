##################
#Practical Comprehensions
##################
#Practical list Comprehension from task 1c1.py

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )
#tupple

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

#List of Latin Names
species_names = [names[0]for names in birds] #List comprehension
print(species_names)

#List of common names
common_names = [common[1]for common in birds] #List comprehension
print(common_names)

#List of mean body massess
body_mass = [body[2]for body in birds]
print(body_mass)

# (2) Now do the same using conventional loops (you can choose to do this 
# before 1 !). 

#List of Latin Names
species_names= []
for names in birds: 
    species_names.append(names[0])
print(species_names)

#List of common names
common_names = []
for common in birds:
    common_names.append(common[1])
print(common_names)

#List of mean body massess
body_mass = []
for body in birds:
    body_mass.append(body[2])
print(body_mass)