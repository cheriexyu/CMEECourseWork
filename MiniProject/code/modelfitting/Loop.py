#!/usr/bin/env python3
#############################
# LOOP FOR ALL SPECIES SUBSET (WITHOUT baranyi)
#############################
from lmfit import Minimizer, Parameters, report_fit
import pandas as pd
import scipy as sc
from scipy import stats 
from scipy.stats import linregress
import numpy as np
import matplotlib.pylab as pl 
import seaborn as sns 

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

#####Cubic
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

linear_minimize = []
linear_residuals = []
linear_params = []
AIC = [] 

for d in range(len(outtime)):
    if len(outtime[d])>4:
        minner = Minimizer(residuals_linear, params_linear, fcn_args=(outtime[d],np.log(outpop[d])))
        fit_linear_NLLS = minner.minimize()
        linear_minimize.append(fit_linear_NLLS)
        linear_residuals.append(fit_linear_NLLS.residual)
        linear_params.append(fit_linear_NLLS.params)
        AIC.append(fit_linear_NLLS.aic)
    else:
        text = 'NA'
        linear_minimize.append(text)
        linear_residuals.append(text)
        linear_params.append(text)
        AIC.append(text)

#####Quadratic
params_quadratic=Parameters() #To store parameters
params_quadratic.add('b2', value = 1)
params_quadratic.add('c2', value = 1)
params_quadratic.add('d2', value = 1)

def residuals_quadratic(params, t, data):
    """Calculate quadratic growth and subtract data"""
    v2 = params.valuesdict()
    model = v2['b2']*t**2 + v2['c2']*t + v2['d2']
    return model - data     

quadratic_minimize = []
quadratic_residuals = []
quadratic_params = []
AIC_quadratic = [] 

for d in range(len(outtime)):
    if len(outtime[d])>3:
        minner_quadratic = Minimizer(residuals_quadratic, params_quadratic, fcn_args=(outtime[d],np.log(outpop[d])))
        fit_quadratic_NLLS = minner_quadratic.minimize()
        quadratic_minimize.append(fit_quadratic_NLLS)
        quadratic_residuals.append(fit_quadratic_NLLS.residual)
        quadratic_params.append(fit_quadratic_NLLS.params)
        AIC_quadratic.append(fit_quadratic_NLLS.aic)
    else:
        text = 'NA'
        quadratic_minimize.append(text)
        quadratic_residuals.append(text)
        quadratic_params.append(text)
        AIC_quadratic.append(text)

#####Gompertz
for d in range(len(outpop)):
    x = outtime[d]
    y = np.log(outpop[d])
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) #calculate slope, r_max
    diff = outtime[d][np.argmax(np.diff(np.diff(np.log(outpop[d]))))] #calculate t_lag
    params_gompertz=Parameters()
    params_gompertz.add_many(('N_0', np.log(outpop[d][-1]) , True, None, None, None, None),('N_max', np.log(max(outpop[d])) , True, None, None, None, None),('r_max', slope, True, None, None, None, None),('t_lag', diff, True, None, None, None, None)) 

def residuals_gompertz(params, t, data):
    v3 = params.valuesdict()
    model = v3['N_0'] + (v3['N_max'] - v3['N_0']) * np.exp(-np.exp(v3['r_max'] * np.exp(1) * (v3['t_lag'] - t) / ((v3['N_max'] - v3['N_0']) * np.log(10)) + 1))
    return model - data 

gompertz_minimize = []
gompertz_residuals = []
gompertz_params = []
AIC_gompertz = [] 

for d in range(len(outtime)):
    if len(outtime[d])>4:
        minner_gompertz = Minimizer(residuals_gompertz, params_gompertz, fcn_args=(outtime[d],np.log(outpop[d])))
        fit_gompertz_NLLS = minner_gompertz.minimize()
        gompertz_minimize.append(fit_gompertz_NLLS)
        gompertz_residuals.append(fit_gompertz_NLLS.residual)
        gompertz_params.append(fit_gompertz_NLLS.params)
        AIC_gompertz.append(fit_gompertz_NLLS.aic)
    else:
        text = 'NA'
        gompertz_minimize.append(text)
        gompertz_residuals.append(text)
        gompertz_params.append(text)
        AIC_gompertz.append(text)


#AIC number output to output CSV
AIC_output = pd.DataFrame(subset,columns=['ID'])
AIC_output['Cubic'] = AIC
AIC_output['Quadratic'] = AIC_quadratic
AIC_output['Gompertz'] = AIC_gompertz
AIC_output.to_csv("../../data/AIC_output.csv",sep=',')

#######GRAPHHHHHHHH
for e in range(len(outpop)): #Cubic
    if len(outtime[e])>4:
        result = np.log(outpop[e]) + linear_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
        pl.plot(outtime[e], result , 'g.', markersize = 8, label = 'Cubic') #plots the datapoints from above
        t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector (x)
        vec=np.ones(len(t_vec)) 
        smooth_line = residuals_linear(linear_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
        pl.plot(t_vec,smooth_line + vec, 'green', linestyle = '--', linewidth = 1) #plot the smooth curve  

    if len(outtime[e])>3: #Quadratic
        result_quadratic = np.log(outpop[e]) + quadratic_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
        pl.plot(outtime[e], result_quadratic , 'y.', markersize = 8, label = 'Quadratic') #plots the datapoints from above
        t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector (x)
        vec=np.ones(len(t_vec)) 
        smooth_line_quadratic = residuals_quadratic(quadratic_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
        pl.plot(t_vec,smooth_line_quadratic + vec, 'orange', linestyle = '--', linewidth = 1) #plot the smooth curve  

    if len(outtime[e])>4: #Gompertz
        result_gompertz = np.log(outpop[e]) + gompertz_residuals[e] #Gompertz 
        pl.plot(outtime[e], result_gompertz, 'b.', markersize = 8, label = 'Gompertz') #datapoints
        t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector (x)
        vec=np.ones(len(t_vec)) 
        residual_smooth_gompertz = residuals_gompertz(gompertz_params[e], t_vec, vec)
        pl.plot(t_vec, residual_smooth_gompertz + vec, 'blue', linestyle = '--', linewidth = 1)

    pl.plot(outtime[e],np.log(outpop[e]), 'k+', markersize = 8,markeredgewidth = 2, label = 'Data', numtostr(e))
    pl.legend(fontsize = 10)
    pl.xlabel('Time(Hours)', fontsize = 10)
    pl.ylabel('Population(log)', fontsize = 10)
    pl.ticklabel_format(style='scientific', scilimits=[0,3])
    pl.show()
