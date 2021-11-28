#!/usr/bin/env python3
#############################
# Data testing for one subset of data (ID 1), PLOTS SUCESSFULLY
#############################

from lmfit import Minimizer, Parameters, report_fit
import pandas as pd
import scipy as sc
from scipy import stats 
from scipy.stats import linregress
import numpy as np
import matplotlib.pylab as pl 
import seaborn as sns 
import csv

#DATA = ID 0

data = pd.read_csv("../../data/editeddata.csv")
print("Loaded {} columns.".format(len(data.columns.values))) #load 10 columns
data = data.drop(columns=['Unnamed: 0'])
data_subset=data[['ID','Time','PopBio','Time_units','PopBio_units']] #data_subset is a subset of data with only the variables we need

#Loop to get subsets of data into a dictionary 
subset = data_subset['ID'].unique()
output = {a: data_subset[data_subset['ID'] == a ]for a in subset}

#Convert time and population column for all subset into a numpy array 
outtime = [output[l]['Time'].to_numpy() for l in range(len(output))]
outpop = [output[l]['PopBio'].to_numpy() for l in range(len(output))] 
outtime = np.asarray(outtime, dtype=object)
outpop = np.asarray(outpop, dtype=object)

#Cubic
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

minner = Minimizer(residuals_linear, params_linear, fcn_args=(outtime[i],np.log(outpop[i])))
fit_linear_NLLS = minner.minimize()
report_fit(fit_linear_NLLS)

#Quadratic
params_quadratic=Parameters() #To store parameters
params_quadratic.add('b2', value = 1)
params_quadratic.add('c2', value = 1)
params_quadratic.add('d2', value = 1)

def residuals_quadratic(params, t, data):
    """Calculate cubic growth and subtract data"""
    #Get an ordered dictionary of parameter values
    v2 = params.valuesdict()
    #Quadratic model
    model = v2['b2']*t**2 + v2['c2']*t + v2['d2']
    return model - data     #Return residuals

minner_quadratic = Minimizer(residuals_quadratic, params_quadratic, fcn_args=(outtime[i],np.log(outpop[i])))
fit_quadratic_NLLS = minner_quadratic.minimize()

#Gompertz Model
x = outtime[i]
y = np.log(outpop[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) #calc regression line using least square 

params_gompertz=Parameters()
params_gompertz.add_many(('N_0', -9349.44228454348 , True, None, None, None, None),('N_max', -1.30860700306332 , True, None, None, None, None),('r_max', 66.5013343232838, True, None, None, None, None),('t_lag', -1042.00126200408, True, None, None, None, None)) 

def residuals_gompertz(params, t, data):
    v = params.valuesdict()
    model = v['N_0'] + (v['N_max'] - v['N_0']) * np.exp(-np.exp(v['r_max'] * np.exp(1) * (v['t_lag'] - t) / ((v['N_max'] - v['N_0']) * np.log(10)) + 1))
    return model - data 

minner = Minimizer(residuals_gompertz, params_gompertz, fcn_args=(outtime[i], np.log(outpop[i])))
fit_gompertz = minner.minimize()
report_fit(fit_gompertz)

# # #Baranyi
# params_baranyi=Parameters()
# params_baranyi.add_many(('N_0', outpop[i][-1] , True, None, None, None, None),('N_max', max(outpop[i]) , True, None, None, None, None),('r_max', slope, True, None, None, None, None),('V', slope , True, None, None, None, None),('M', 1, True, None, None, None, None),('t_lag', (outtime[i][np.argmax(np.diff(np.diff(np.log(outpop[i]))))]), True, None, None, None, None))  #h_0 = lag time * growth rate 

# def residuals_baranyi(params, t, data):
#     v4 = params.valuesdict()
#     model3 = t + (1 / v4['V']) * np.log( np.exp(-v4['V'] * t) + np.exp((-v4['t_lag'] * v4['r_max']) - np.exp(((-v4['V']) * t) - (v4['t_lag'] * v4['r_max']))))
#     model = v4['N_0'] + v4['r_max'] * model3 - ( 1 / v4['M'] ) * np.log ( 1 + ((( np.exp(v4['r_max'] * model3)) - 1 ) / (np.exp(v4['M'] * (v4['N_max'] - v4['N_0'])))))
#     return model - data 

# minner_baranyi = Minimizer(residuals_baranyi, params_baranyi, fcn_args=(outtime[i], np.log(outpop[i])))
# fit_baranyi = minner_baranyi.minimize()
# report_fit(fit_baranyi)

#GRAPHHHHHHHH
f1 = pl.figure()

result_quadratic = np.log(outpop[i]) + fit_quadratic_NLLS.residual # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
pl.plot(outtime[i], result_quadratic , 'y.', markersize = 8, label = 'Quadratic') #plots the datapoints from above
t_vec = np.linspace(0,max(outtime[i]),1000)
vec = np.ones(len(t_vec))
smooth_line_quadratic = residuals_quadratic(fit_quadratic_NLLS.params,t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
pl.plot(t_vec,smooth_line_quadratic + vec, 'orange', linestyle = '--', linewidth = 1)

result = np.log(outpop[i]) + fit_linear_NLLS.residual # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
pl.plot(outtime[i], result , 'g.', markersize = 8, label = 'Cubic') #plots the datapoints from above
t_vec = np.linspace(0,max(outtime[i]),1000)
vec = np.ones(len(t_vec))
smooth_line = residuals_linear(fit_linear_NLLS.params,t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
pl.plot(t_vec,smooth_line + vec, 'green', linestyle = '--', linewidth = 1)

result_gompertz = np.log(outpop[i]) + fit_gompertz.residual #Gompertz 
pl.plot(outtime[i], result_gompertz, 'b.', markersize = 8, label = 'Gompertz') #datapoints
t_vec = np.linspace(0,max(outtime[i]),1000)
vec = np.ones(len(t_vec))
residual_smooth_gompertz = residuals_gompertz(fit_gompertz.params, t_vec, vec)
pl.plot(t_vec, residual_smooth_gompertz + vec, 'blue', linestyle = '--', linewidth = 1)

# result_baranyi = np.log(outpop[i]) + fit_baranyi.residual
# pl.plot(outtime[i], result_baranyi, '.', markerfacecolor = 'magenta', markeredgecolor = 'magenta', markersize = 8, label = 'Baranyi')
# t_vec = np.linspace(0,max(outtime[i]),1000)
# vec = np.ones(len(t_vec))
# residual_smooth_baranyi = residuals_baranyi(fit_baranyi.params, t_vec, vec)
# pl.plot(t_vec, residual_smooth_baranyi + vec, 'magenta', linestyle = '--', linewidth = 1)

pl.plot(outtime[i],np.log(outpop[i]), 'k+', markersize = 8,markeredgewidth = 2, label = 'Data')
pl.legend(fontsize = 10)
pl.xlabel('Time(Hours)', fontsize = 10)
pl.ylabel('Population(log)', fontsize = 10)
pl.ticklabel_format(style='scientific', scilimits=[0,3])
pl.show()

f1.savefig('test_ID_1.pdf') 