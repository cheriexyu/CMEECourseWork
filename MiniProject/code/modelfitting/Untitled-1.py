#!/usr/bin/env python3
#############################
# Sample Data
#############################
#Gompertz 
from lmfit import Minimizer, Parameters, report_fit
import pandas as pd
import scipy as sc
from scipy import stats 
from scipy.stats import linregress
import numpy as np
import matplotlib.pylab as pl 
import seaborn as sns 

data = pd.read_csv("../../data/editeddata.csv")
#print("Loaded {} columns.".format(len(data.columns.values))) #load 10 columns
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

test = pd.DataFrame(data=subset,columns=['ID'])
test['outpop'] = outpop
test['outtime'] = outtime
test.set_index('ID', inplace=True)
test.drop([4,14,16,20,88,280,281,282,283,284],inplace=True)
test = test.reset_index()

# test = pd.read_csv("../../data/data_after_sample_gompertz.csv")
# test["outpop"]
outpop_test = test["outpop"].to_numpy()
outtime_test = test["outtime"].to_numpy()
ID = test["ID"].to_numpy()

slope_r_max=[]

#gompertz_minimize = []
#gompertz_residuals = [] #all these are 27500
params = [] #all these are 27500
alloc = np.zeros((275,4)) 

for d in range(len(outtime_test)):
    print(d)
    x = outtime_test[d]
    y = np.log(outpop_test[d])
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) #calc r_max 
    slope_r_max.append(slope)

    #Draw a normal distribution
    np.random.seed(1234) #seed to 1234
    mu, sigma = slope_r_max[d], 0.1
    s = np.random.normal(mu, sigma, 100) # 100 numbers output random sample r max 
    #gompertz_params_minimize = [] #Minimized parameters for storing
    x_big = np.inf 

    for i in range(len(s)):
    
        params_logistic=Parameters()
        params_logistic.add_many(('N_0', outpop_test[d][-1] , True, None, None, None, None),('N_max', max(outpop_test[d]) , True, None, None, None, None),('r_max', s[i], True, None, None, None, None)) 
        params.append(params_logistic)

        def residuals_logistic(params, t, data):
            v = params.valuesdict()
            model = np.log(v['N_0'] * v['N_max'] * np.exp(v['r']*t) / (v['N_max'] + v['N_0'] * ( np.exp(v['r']*t) - 1 )))
            return model - data
        
        try:
            if len(outtime_test[d])>3:
                minner = Minimizer(residuals_logistic, params[d], fcn_args=(outtime_test, np.log(outpop_test[d])))#Plug in the logged data.
                fit_logistic = minner.minimize(method = 'leastsq')
                par_dict = fit_logistic.params.valuesdict()
                values = np.fromiter(par_dict.values(), dtype=float)
                x = fit_logistic.aic
                values = np.append(values,x)
                if x < x_big:
                    alloc[d] = values
                    x_big = x
        
            else:
                text = np.nan
                alloc[d] = text
                #gompertz_minimize.append(text)
                #gompertz_residuals.append(text)
                #gompertz_params_minimize.append(text)
    
        except Exception:
            print(f"This didn't work; d = {d}") # DID not work for subset 280 to 284 



error = []
for d in range(len(outtime_test)):
    try:
        print(d)
        x = outtime_test[d]
        y = np.log(outpop_test[d])
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) #calc r_max 
        slope_r_max.append(slope)
        params_logistic=Parameters()
        params_logistic.add_many(('N_0', outpop_test[d][-1] , True, None, None, None, None),('N_max', max(outpop_test[d]) , True, None, None, None, None),('r_max', s[i], True, None, None, None, None)) 
        params.append(params_logistic)

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
        







