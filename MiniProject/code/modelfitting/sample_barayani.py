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

outpop_test = test["outpop"].to_numpy()
outtime_test = test["outtime"].to_numpy()
ID = test["ID"].to_numpy()

#data_subset=data[['ID','Time','PopBio','Time_units','PopBio_units']] #data_subset is a subset of data with only the variables we need

#Loop to get subsets of data into a dictionary 
#subset = data_subset['ID'].unique()
#output = {a: data_subset[data_subset['ID'] == a ]for a in subset}

#Convert time and population column for all subset into a numpy array 
#outtime = [output[l]['Time'].to_numpy() for l in range(len(output))]
#outpop = [output[l]['PopBio'].to_numpy() for l in range(len(output))] 
#outtime = np.asarray(outtime, dtype=object)
#outpop = np.asarray(outpop, dtype=object)

#SAMPLING
slope_r_max_b=[]
diff_lag_b=[]

#baranyi_minimize = []
#baranyi_residuals = []
#baranyi_params_minimize = [] #Minimized parameters for storing
#AIC_gompertz = [] 
params_b = []
alloc_baranyi = np.zeros((275,6))

for f in range(len(outtime_test)):
    print(f)
    x = outtime_test[f]
    y = np.log(outpop_test[f])
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) #calc r_max 
    diff = outtime_test[f][np.argmax(np.diff(np.diff(np.log(outpop_test[f]))))] #calct_lag
    slope_r_max_b.append(slope)
    diff_lag_b.append(diff)

    #Draw a normal distribution
    np.random.seed(1234) #seed to 1234
    mu, sigma = slope_r_max_b[f], 0.5
    s = np.random.normal(mu, sigma, 1000) # 100 numbers output random sample r max 
    mu2, sigma2 = diff_lag_b[f], 0.5
    k = np.random.normal(mu2, sigma2, 1000) # 100 numbers out random sample lag time
    x_big = np.inf

    for j in range(len(s)):

        params_baranyi=Parameters()
        params_baranyi.add_many(('N_0', outpop_test[f][-1] , True, -1000000, 1000000, None, None),('N_max', max(outpop_test[f]) , True, -1000000, 1000000, None, None),('r_max', s[j], True, -1000, 1000, None, None),('h_0', s[j] * k[j] , True, None, None, None, None ))
        params_b.append(params_baranyi)

        def residuals_baranyi(params, t, data):
            v4 = params.valuesdict()
            A = t + (1/v4['r_max']) * np.log(np.exp(-(v4['r_max']) * t) + np.exp(-(v4['h_0'])) - np.exp((-v4['r_max']) * t - v4['h_0'])) 
            model = np.log(v4['N_0']) + v4['r_max'] * A - np.log(1 + (np.exp(v4['r_max'] * A) - 1) / np.exp(np.log(v4['N_max']) - np.log(v4['N_0'])))
            #model = np.log(model)
            return model - data 
        try:
            if len(outtime_test[f])>4:
                minner_baranyi = Minimizer(residuals_baranyi, params_b[f], fcn_args=(outtime_test[f], np.log(outpop_test[f])))
                fit_baranyi_NLLS = minner_baranyi.minimize() #THIS IS THE SENSITIVE PART
                #gompertz_minimize.append(fit_gompertz_NLLS)
                #gompertz_residuals.append(fit_gompertz_NLLS.residual)
                #gompertz_params_minimize.append(fit_gompertz_NLLS.params)
                #AIC_gompertz.append(fit_gompertz_NLLS.aic) 
                par_dict_b = fit_baranyi_NLLS.params.valuesdict()
                values_b = np.fromiter(par_dict_b.values(), dtype=float)
                x = fit_baranyi_NLLS.aic
                values_b = np.append(values_b,x)
                if x < x_big:
                    alloc_baranyi[f] = values_b
                    x_big = x
            
            else:
                text = np.nan
                alloc_baranyi[d] = text
    
        except Exception:
            print(f"This didn't work; f = {f}")

df3 = pd.DataFrame(alloc_baranyi)
df3.to_csv("../../data/test.csv", sep=',',na_rep="NaN")
