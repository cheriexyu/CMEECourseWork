#!/usr/bin/env python3
##################
#Practical Comprehensions
##################

# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.

rain = [i for i in rainfall if i[1]>100]
print(rain)

# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 

month = [a[0] for a in rainfall if a[1]<50]
print(month)

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 

#(1)
rain = []
for i in rainfall:
    if i[1]>100:
        rain.append(i)
print(rain)

#(2)
month = []
for a in rainfall:
    if a[1]<50:
        month.append(a[0])
print(month)

