#!/usr/bin/env python3
#############################
# try and catch
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

###########################################Gompertz

def residuals_gompertz(params, t, data):
    v3 = params.valuesdict()
    model = v3['N_0'] + (v3['N_max'] - v3['N_0']) * np.exp(-np.exp(v3['r_max'] * np.exp(1) * (v3['t_lag'] - t) / ((v3['N_max'] - v3['N_0']) * np.log(10)) + 1))
    return model - data 

gompertz_minimize = []
gompertz_residuals = []
gompertz_params_minimize = [] #Minimized parameters for storing
AIC_gompertz = [] 
params = [] #Storing starting points for parameters


# #CALC DIFF _t _lag
# np.diff(np.diff(np.log(outpop[d])))
# [np.argmax(np.diff(np.diff(np.log(outpop[d]))))] #position of the largest max 
# max((np.diff(np.diff(np.log(outpop[d])))))
# outtime[d][np.argmax(np.diff(np.diff(np.log(outpop[d]))))]
# outpop[0]
# outtime[0]

# len(outpop[d])
# x = (np.diff(np.diff(np.log(outpop[0])))) #difference of differences 
# [np.argmax(np.diff(np.diff(np.log(outpop[d]))))] #position of the largest max , 15 - 16 
# cut = outpop[0][16:29]


###########
#(NAME VALUE VARY MIN  MAX  EXPR  BRUTE_STEP)

error = []
for d in range(len(outtime)):
    try:
        x = outtime[d]
        y = np.log(outpop[d])
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) #calculate slope, r_max
        diff = outtime[d][np.argmax(np.diff(np.diff(np.log(outpop[d]))))] #calculate t_lag
        params_gompertz=Parameters()
        params_gompertz.add_many(('N_0', np.log(outpop[d][-1]) , True, None, None, None, None),('N_max', np.log(max(outpop[d])) , True, None, None, None, None),('r_max', slope, True, None, None, None, None),('t_lag', diff, True, None, None, None, None)) 
        params.append(params_gompertz)

        if len(outtime[d])>4:
            minner_gompertz = Minimizer(residuals_gompertz, params[d], fcn_args=(outtime[d],np.log(outpop[d])))
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
    except:
        print(f"This didn't work; d = {d}")
        error.append(d) #86 IDs Does not Work 
        









############################################ #Notes
#             result_gompertz = np.log(outpop[e]) + gompertz_residuals[e] #Gompertz 
#             pl.plot(outtime[e], result_gompertz, 'b.', markersize = 8, label = 'Gompertz') #datapoints
#             t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector (x)
#             vec=np.ones(len(t_vec)) 
#             residual_smooth_gompertz = residuals_gompertz(gompertz_params_minimize[e], t_vec, vec)
#             pl.plot(t_vec, residual_smooth_gompertz + vec, 'blue', linestyle = '--', linewidth = 1)

#             pl.plot(outtime[e],np.log(outpop[e]), 'k+', markersize = 8,markeredgewidth = 2, label = 'Data')
#             pl.legend(fontsize = 10)
#             pl.xlabel('Time(Hours)', fontsize = 10)
#             pl.ylabel('Population(log)', fontsize = 10)
#             pl.ticklabel_format(style='scientific', scilimits=[0,3])
#             pl.show()

#Barayani

def residuals_baranyi(params, t, data):
    v4 = params.valuesdict()
    model3 = t + (1 / v4['V']) * np.log( np.exp(-v4['V'] * t) + np.exp((-v4['t_lag'] * v4['r_max']) - np.exp(((-v4['V']) * t) - (v4['t_lag'] * v4['r_max']))))
    model = v4['N_0'] + v4['r_max'] * model3 - ( 1 / v4['M'] ) * np.log ( 1 + ((( np.exp(v4['r_max'] * model3)) - 1 ) / (np.exp(v4['M'] * (v4['N_max'] - v4['N_0'])))))
    return model - data 

baranyi_minimize = []
baranyi_residuals = []
baranyi_params_minimize = []
AIC_baranyi = [] 
params_b = []

error_barayani = []

for p in range(len(outpop)):
    try:
        x = outtime[p]
        y = np.log(outpop[p])
        slope_baranyi, intercept, r_value, p_value, std_err = stats.linregress(x,y) #calculate slope, r_max
        params_baranyi=Parameters()
        params_baranyi.add_many(('N_0', outpop[p][-1] , True, None, None, None, None),('N_max', max(outpop[p]) , True, None, None, None, None),('r_max', slope_baranyi, True, None, None, None, None),('V', slope_baranyi , True, None, None, None, None),('M', 1, True, None, None, None, None),('t_lag', (outtime[p][np.argmax(np.diff(np.diff(np.log(outpop[p]))))]), True, None, None, None, None))  #h_0 = lag time * growth rate 
        params_b.append(params_baranyi)
        if len(outtime[p])>5:
            minner_baranyi = Minimizer(residuals_baranyi, params_b[p], fcn_args=(outtime[p], np.log(outpop[p])))
            fit_baranyi = minner_baranyi.minimize()
            baranyi_minimize.append(fit_baranyi)
            baranyi_residuals.append(fit_baranyi.residual)
            baranyi_params_minimize.append(fit_baranyi.params)
            AIC_baranyi.append(fit_baranyi.aic)
        else:
            text = 'NA'
            baranyi_minimize.append(text)
            baranyi_residuals.append(text)
            baranyi_params_minimize.append(text)
            AIC_baranyi.append(text)
    except:
        print(f"This didn't work; p = {p}")
        error_barayani.append(p) #Does not work for 184 IDs
