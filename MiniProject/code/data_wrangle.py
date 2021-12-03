#!/usr/bin/env python3
#############################
# Data Wrangling
#############################

import pandas as pd

#two main fields of interest are Popbio and time 
data = pd.read_csv("../data/LogisticGrowthData.csv") #Load data
print("Loaded {} columns.".format(len(data.columns.values))) #load 10 columns

data.insert(0, "ID", data.Species + "_" + data.Temp.map(str) + "_" + data.Medium + "_" + data.Citation) #filters it by same species first 

#print(data.ID.unique()) #Creating ID from numbers instead of long list 
data['ID'] = pd.factorize(data.ID)[0]

print(data['ID']) # data has been ID from number 0 to 284

data.isnull().values.any() #Check if there is any NaN

#Get rid of negative values in time column 
data = data[data['Time'] > 0]

#Get rid of negative values in pop column 
data = data[data['Time'] > 0]

data.to_csv("../data/editeddata.csv", sep=',') #save to csv



test = data
test.set_index('ID', inplace=True)
test.drop([4,14,16,20,88,280,281,282,283,284],inplace=True) #get rid of ID that cannot be minimized according the gompertz sampling 
test = test.reset_index()
test
Sample_size = test.groupby('ID').size().sort_values().reset_index(name='Sample_Size')
Sample_size.set_index('ID', inplace=True)
Sample_size.to_csv("../data/sample_size.csv", sep=',') #isolate the sample sizes into a csv 

