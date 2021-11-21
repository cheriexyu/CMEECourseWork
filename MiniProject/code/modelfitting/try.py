#!/usr/bin/env python3
#############################
# Data testing for ID 0 to model linear 
#############################

from lmfit import Minimizer, Parameters, report_fit
import pandas as pd
import scipy as sc 
import numpy as np
import matplotlib.pylab as pl 
import seaborn as sns 

data = pd.read_csv("../../data/editeddata.csv")
print("Loaded {} columns.".format(len(data.columns.values))) #load 10 columns
data = data.drop(columns=['Unnamed: 0'])
data.head()

#ID_0 = data[data['ID']==0] #How to subset data to only get ID 0 with all columns 
#ID_0 

data_subset=data[['ID','Time','PopBio','Time_units','PopBio_units']] #data_subset is a subset of data with only the variables we need

ID_0 = data_subset[data['ID']==0] #getting data for only variables we need 
ID_0 
sns.lmplot(x='Time',y='PopBio',data=ID_0,fit_reg=False) #FOR ID 0 
pl.show() #show graph

#Convert the columns into an array 
time_0 = ID_0['Time'].to_numpy()
popbio_0 = ID_0['PopBio'].to_numpy()

#Fiting a phenomenological linear Cubic Equation using NLLS
params_linear=Parameters() #To store parameters
params_linear.add('a', value = 1)
params_linear.add('b', value = 1)
params_linear.add('c', value = 1)
params_linear.add('d', value = 1)

def residuals_linear(params, t, data):
    """Calculate cubic growth and subtract data"""
    #Get an ordered dictionary of parameter values
    v = params.valuesdict()
    #Cubic model
    model = v['a']*t**3 + v['b']*t**2 + v['c']*t + v['d']
    return model - data     #Return residuals

minner = Minimizer(residuals_linear, params_linear, fcn_args=(time_0, popbio_0))
fit_linear_NLLS = minner.minimize()

report_fit(fit_linear_NLLS)

#extract estimated parameter values in a dictionary then into a list
par_dict = fit_linear_NLLS.params.valuesdict().values()
par = np.array(list(par_dict))

#calculate residuals
print(par)
def equation(l):
    model2 = par[0]*l**3 + par[1]*l**2 + par[2]*l + par[3]
    return model2
y = equation(time_0)

residuals = y - popbio_0
print(residuals)

#Plot the fitted result
pl.rcParams['figure.figsize'] = [10, 15] #set up figure enivornment with width and height #NEED TO FIGURE THIS OUT
result = popbio_0 + fit_linear_NLLS.residual #these point lay on top of the theoretical ones  
pl.plot(time_0,result, 'y.', markersize = 10, label = 'Quadratic')
t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector
vec=np.ones(len(t_vec)) #creates a vector of one why?
smooth_line = residuals_linear(fit_linear_NLLS.params,t_vec,vec)
pl.plot(t_vec,smooth_line + vec, 'orange', linestyle = '--', linewidth = 1) #Why do you add a vector one
pl.plot(time_0,popbio_0, 'r+', markersize = 10,markeredgewidth = 2, label = 'Data')
pl.legend(fontsize = 10)
pl.xlabel('Time(Hours)', fontsize = 10)
pl.ylabel('Population', fontsize = 10)
pl.ticklabel_format(style='scientific', scilimits=[0,3])
pl.show()

#Dont even need to hand calculate residuals 
#Should I make the axis better? 700 hours mean nothing and should i log the 7 axis?

