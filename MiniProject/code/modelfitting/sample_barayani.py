#!/usr/bin/env python3
#############################
# Sample Data 
#############################
#Barayani

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

#SAMPLING
slope_r_max=[]
diff_lag=[]

baranyi_minimize = []
baranyi_residuals = []
baranyi_params_minimize = [] #Minimized parameters for storing
#AIC_gompertz = [] 
params_baranyi = []
alloc_baranyi = np.zeros(280)

for f in range(len(outtime)):
    print(f)
    x = outtime[f]
    y = np.log(outpop[f])
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) #calc r_max 
    diff = outtime[f][np.argmax(np.diff(np.diff(np.log(outpop[f]))))] #calct_lag
    slope_r_max.append(slope)
    diff_lag.append(diff)

    #Draw a normal distribution
    mu, sigma = slope_r_max[f], 0.1
    s = np.random.normal(mu, sigma, 100) # 100 numbers output random sample r max 
    mu2, sigma2 = diff_lag[f], 0.1
    k = np.random.normal(mu2, sigma2, 100) # 100 numbers out random sample lag time

    for j in range(len(s)):
    
        params_baranyi=Parameters()
        params_baranyi.add_many(('N_0', outpop[f][-1] , True, None, None, None, None),('N_max', max(outpop[f]) , True, None, None, None, None),('r_max', s[j], True, None, None, None, None),('V', s[j] , True, None, None, None, None),('M', 1, True, None, None, None, None),('t_lag', diff[j], True, None, None, None, None)) 
        params_baranyi.append(params_baranyi)

        def residuals_baranyi(params, t, data):
            v4 = params.valuesdict()
            model3 = t + (1 / v4['V']) * np.log( np.exp(-v4['V'] * t) + np.exp((-v4['t_lag'] * v4['r_max']) - np.exp(((-v4['V']) * t) - (v4['t_lag'] * v4['r_max']))))
            model = v4['N_0'] + v4['r_max'] * model3 - ( 1 / v4['M'] ) * np.log ( 1 + ((( np.exp(v4['r_max'] * model3)) - 1 ) / (np.exp(v4['M'] * (v4['N_max'] - v4['N_0'])))))
            return model - data

        try:
            if len(outtime[f])>4:
                minner_baranyi = Minimizer(residuals_baranyi, params_baranyi[f], fcn_args=(outtime[f],np.log(outpop[f])))
                fit_gompertz_NLLS = minner_gompertz.minimize() #THIS IS THE SENSITIVE PART
                gompertz_minimize.append(fit_gompertz_NLLS)
                gompertz_residuals.append(fit_gompertz_NLLS.residual)
                gompertz_params_minimize.append(fit_gompertz_NLLS.params)
                #AIC_gompertz.append(fit_gompertz_NLLS.aic) 
            
            else:
                text = np.nan
                gompertz_minimize.append(text)
                gompertz_residuals.append(text)
                gompertz_params_minimize.append(text)
                AIC_gompertz.append(text)
    
        except Exception:
            print(f"This didn't work; f = {f}")

    alloc[f] = (np.min(fit_gompertz_NLLS.aic)) 
    