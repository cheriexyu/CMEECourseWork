#!/usr/bin/env python3
#############################
# Data edit
#############################

import pandas as pd
import scipy as sc 
import matplotlib.pylab as pl 
import seaborn as sns 

#two main fields of interest are Popbio and time 
data = pd.read_csv("../../data/LogisticGrowthData.csv")
print("Loaded {} columns.".format(len(data.columns.values))) #load 10 columns

print(data.columns.values) #column names
data.head()

print(data.PopBio_units.unique()) #all units in population measurements , need to change it to the same?
print(data.Time_units.unique()) #units of the independnt variable "Hours"

data.insert(0, "ID", data.Species + "_" + data.Temp.map(str) + "_" + data.Medium + "_" + data.Citation) #filters it by same specieis first 

print(data.columns.values)
data.head()

print(data.ID.unique()) #Creating ID from numbers instead of long list 
data['ID'] = pd.factorize(data.ID)[0]

print(data['ID']) # data has been ID from number 0 to 284

ID_0 = data[data['ID']==0] #How to subset data to only get ID 0 with all columns 
ID_0

data_subset=data[['ID','Time','PopBio','Time_units','PopBio_units']] #data_subset is a subset of data with only the variables we need

ID_0 = data_subset[data['ID']==0] #getting data for only variables we need 
ID_0 

sns.lmplot("Time","PopBio",data=ID_0,fit_reg=False) #FOR ID 0 
pl.show() #show graph

data.isnull().values.any() #Check if there is any NaN


data.to_csv("../../data/editeddata.csv", sep=',')