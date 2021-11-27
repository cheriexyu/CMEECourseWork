#!/usr/bin/env python3
#############################
# Sample Data
#############################
#Gompertz Model Fitting
from lmfit import Minimizer, Parameters, report_fit
import pandas as pd
import scipy as sc
from scipy import stats 
from scipy.stats import linregress
import numpy as np
import matplotlib.pylab as pl 
import seaborn as sns 

data = pd.read_csv("../../data/editeddata.csv")
data = data.drop(columns=['Unnamed: 0'])
data_subset=data[['ID','Time','PopBio','Time_units','PopBio_units']] #data_subset is a subset of data with only the variables we need

#Loop to get subsets of data into a dictionary 
subset = data_subset['ID'].unique()
output = {a: data_subset[data_subset['ID'] == a ]for a in subset}

#Get rid of the data that showed NA during model fitting (less than 4 parameters)
data_subset=data[['ID','Time','PopBio','Time_units','PopBio_units']] #data_subset is a subset of data with only the variables we need

#Convert time and population column for all subset into a numpy array 
outtime = [output[l]['Time'].to_numpy() for l in range(len(output))]
outpop = [output[l]['PopBio'].to_numpy() for l in range(len(output))] 
outtime = np.asarray(outtime, dtype=object)
outpop = np.asarray(outpop, dtype=object)

# data2 = pd.read_csv("../../data/data_gompertz.csv")
# data2 = data2.drop(columns=['Unnamed: 0'])
# data_subset2=data2[['ID','Time','PopBio','Time_units','PopBio_units']] #data_subset is a subset of data with only the variables we need
# subset = data_subset2['ID'].unique()
# output = {a: data_subset2[data_subset2['ID'] == a ]for a in subset}
# outtime = [output[l]['Time'].to_numpy() for l in range(len(output))]
# outpop = [output[l]['PopBio'].to_numpy() for l in range(len(output))] 
# outtime = np.asarray(outtime, dtype=object)
# outpop = np.asarray(outpop, dtype=object)
##################

data = pd.read_csv("../../data/minimized_paras_gompertz.csv")
data = data.drop(columns=['Unnamed: 0']) #original data of parameters + aic
parameters = data.iloc[: , :-1] #dataframe of only parameters
parameters_array = parameters.to_numpy() #minimized parameters as np.array
len(parameters_array)
# test = pd.DataFrame(outtime,outpop,parameters)
# test = parameters.dropna(axis=0, how='all',inplace=False)
# outtime_gompertz = outtime[0:280] #make same length to the minimized parameters 
# outpop_gompertz = outpop[0:280]


test = parameters
test['Time'] = outtime[0:280]
test['PopBio'] = outpop[0:280]
test.dropna(axis=0,how='any',inplace=True)
test

outpop_noNAN = test["PopBio"].to_numpy()
len(outpop_noNAN)
outtime_noNAN = test["Time"].to_numpy()
len(outtime_noNAN)
parameters_noNAN = test[["N_0","N_max","r_max","t_lag"]].to_numpy()


outpop_noNAN
outtime_noNAN
parameters_noNAN





params = []
gompertz_residuals = []
gompertz_params_minimize = [] #Minimized parameters for storing
AIC_gompertz = [] 

def residuals_gompertz(params, t, data):
    v3 = params.valuesdict()
    model = v3['N_0'] + (v3['N_max'] - v3['N_0']) * np.exp(-np.exp(v3['r_max'] * np.exp(1) * (v3['t_lag'] - t) / ((v3['N_max'] - v3['N_0']) * np.log(10)) + 1))
    return model - data 

for e in range(len(outtime_noNAN)):
    print(e)
    params_gompertz=Parameters()
    params_gompertz.add_many(('N_0', np.log(parameters_noNAN[e][0]) , True, None, None, None, None),('N_max', np.log(parameters_noNAN[e][1]) , True, None, None, None, None),('r_max', parameters_noNAN[e][2], True, None, None, None, None),('t_lag', parameters_noNAN[e][3], True, None, None, None, None)) 
    params.append(params_gompertz)
    minner_gompertz = Minimizer(residuals_gompertz, params[e], fcn_args=(outtime_noNAN[e],np.log(outpop_noNAN[e]))) #change outime_gomperts and outpop length to without the NAS
        
    fit_gompertz_NLLS = minner_gompertz.minimize()
    gompertz_residuals.append(fit_gompertz_NLLS.residual)
    gompertz_params_minimize.append(fit_gompertz_NLLS.params)
    AIC_gompertz.append(fit_gompertz_NLLS.aic)





# else:
#         print(f"NaN values in subset ID {e}")

len(params)
len(outtime_gompertz)








for e in range(len(outtime_gompertz[e])):
    #if not na
    result_gompertz = np.log(outpop_gompertz[g]) + gompertz_residuals[g] #Gompertz 
    pl.plot(outtime_gompertz[g], result_gompertz, 'b.', markersize = 8, label = 'Gompertz') #datapoints
    t_vec=np.linspace(0,max(outtime_gompertz[g]),1000) #to get a smooth curve we need to plug in our own time vector (x)
        vec=np.ones(len(t_vec)) 
        residual_smooth_gompertz = residuals_gompertz(gompertz_params_minimize[g], t_vec, vec)
        pl.plot(t_vec, residual_smooth_gompertz + vec, 'blue', linestyle = '--', linewidth = 1)



'N_0' = parameters[e][0]








gompertz_minimize = []
gompertz_residuals = []
gompertz_params_minimize = [] #Minimized parameters for storing
AIC_gompertz = [] 
params = [] #Storing starting points for parameters


for e in range(len(outpop_gompertz)):
    params_gompertz=Parameters()
    params_gompertz.add_many(('N_0', parameters[e][0] , True, None, None, None, None),('N_max', parameters[e][1] , True, None, None, None, None),('r_max', parameters[e][2], True, None, None, None, None),('t_lag', parameters[e][3], True, None, None, None, None)) 
    params.append(params_gompertz)

    if len(outtime_gompertz[e])>4:
        minner_gompertz = Minimizer(residuals_gompertz, params[e], fcn_args=(outtime_gompertz[e],np.log(outpop_gompertz[e])))
        fit_gompertz_NLLS = minner_gompertz.minimize()
        gompertz_minimize.append(fit_gompertz_NLLS)
        gompertz_residuals.append(fit_gompertz_NLLS.residual)
        gompertz_params_minimize.append(fit_gompertz_NLLS.params)
        AIC_gompertz.append(fit_gompertz_NLLS.aic)

    else:
        text = 'NA'
        gompertz_minimize.append(text)
        gompertz_residuals.append(text)
        gompertz_params_minimize.append(text)
        AIC_gompertz.append(text)



for g in range(len(outpop_gompertz)):
    if len(outtime_gompertz[g])>4: #Gompertz
        result_gompertz = np.log(outpop_gompertz[g]) + gompertz_residuals[g] #Gompertz 
        pl.plot(outtime_gompertz[g], result_gompertz, 'b.', markersize = 8, label = 'Gompertz') #datapoints
        t_vec=np.linspace(0,max(outtime_gompertz[g]),1000) #to get a smooth curve we need to plug in our own time vector (x)
        vec=np.ones(len(t_vec)) 
        residual_smooth_gompertz = residuals_gompertz(gompertz_params_minimize[g], t_vec, vec)
        pl.plot(t_vec, residual_smooth_gompertz + vec, 'blue', linestyle = '--', linewidth = 1)

    pl.plot(outtime_gompertz[g],np.log(outpop_gompertz[g]), 'k+', markersize = 8,markeredgewidth = 2, label = 'Data')
    pl.legend(fontsize = 10)
    pl.xlabel('Time(Hours)', fontsize = 10)
    pl.ylabel('Population(log)', fontsize = 10)
    pl.ticklabel_format(style='scientific', scilimits=[0,3])
    pl.show(block=False)
