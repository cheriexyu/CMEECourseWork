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

#New data set of n=275 after getting rid of data that don't fit
test = pd.DataFrame(data=subset,columns=['ID'])
test['outpop'] = outpop
test['outtime'] = outtime
test.set_index('ID', inplace=True)
test.drop([4,14,16,20,88,280,281,282,283,284],inplace=True)
test = test.reset_index()

outpop_test = test["outpop"].to_numpy()
outtime_test = test["outtime"].to_numpy()
ID = test["ID"].to_numpy()

#######SAMPLE
slope_r_max=[]
diff_lag=[]

gompertz_minimize = []
gompertz_residuals = []
params = []
alloc = np.zeros((275,5))

for d in range(len(outtime_test)):
    print(d)
    x = outtime_test[d]
    y = np.log(outpop_test[d])
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) #calc r_max 
    diff = outtime_test[d][np.argmax(np.diff(np.diff(np.log(outpop_test[d]))))] #calct_lag
    slope_r_max.append(slope)
    diff_lag.append(diff)

    #Draw a normal distribution
    np.random.seed(1234) #seed to 1234
    mu, sigma = slope_r_max[d], 0.1
    s = np.random.normal(mu, sigma, 100) # 100 numbers output random sample r max 
    mu2, sigma2 = diff_lag[d], 0.1
    k = np.random.normal(mu2, sigma2, 100) # 100 numbers out random sample lag time
    #gompertz_params_minimize = [] #Minimized parameters for storing
    x_big = np.inf

    for i in range(len(s)):
    
        params_gompertz=Parameters()
        params_gompertz.add_many(('N_0', np.log(outpop_test[d][-1]) , True, None, None, None, None),('N_max', np.log(max(outpop_test[d])) , True, None, None, None, None),('r_max', s[i], True, None, None, None, None),('t_lag', k[i], True, None, None, None, None)) 
        params.append(params_gompertz)

        def residuals_gompertz(params, t, data):
            v = params.valuesdict()
            model = v['N_0'] + (v['N_max'] - v['N_0']) * np.exp(-np.exp(v['r_max'] * np.exp(1) * (v['t_lag'] - t) / ((v['N_max'] - v['N_0']) * np.log(10)) + 1))
            return model - data 

        try:
            if len(outtime_test[d])>4:
                minner_gompertz = Minimizer(residuals_gompertz, params[d], fcn_args=(outtime_test[d],np.log(outpop_test[d])))
                fit_gompertz_NLLS = minner_gompertz.minimize() #THIS IS THE SENSITIVE PART
                #gompertz_minimize.append(fit_gompertz_NLLS)
                gompertz_residuals.append(fit_gompertz_NLLS.residual)
                par_dict = fit_gompertz_NLLS.params.valuesdict()
                values = np.fromiter(par_dict.values(), dtype=float)
                x = fit_gompertz_NLLS.aic
                values = np.append(values,x)
                if x < x_big:
                    alloc[d] = values
                    x_big = x

            else:
                text = np.nan
                alloc[d] = text
                #gompertz_minimize.append(text)
                gompertz_residuals.append(text)
                #gompertz_params_minimize.append(text)
    
        except Exception:
            print(f"This didn't work; d = {d}") # DID not work for subset 280 to 284 
    

df2 = pd.DataFrame(alloc) #save parameters and AIC to csv 
df2.columns = ['N_0', 'N_max','r_max','t_lag','AIC'] 
df2.insert(0, 'ID', ID)
df2.set_index('ID', inplace=True)

df2
df2.to_csv("../../data/minimized_paras_gompertz.csv", sep=',',na_rep="NaN")





for f in range(len(outtime_test)):
    if len(outtime_test[f])>4: #Gompertz
        result_gompertz = np.log(outpop_test[f]) + gompertz_residuals[f] #Gompertz 
        pl.plot(outtime_test[e], result_gompertz, 'b.', markersize = 8, label = 'Gompertz') #datapoints
        t_vec=np.linspace(0,outtime_test[e],1000) #to get a smooth curve we need to plug in our own time vector (x)
        vec=np.ones(len(t_vec)) 
        residual_smooth_gompertz = residuals_gompertz(#gompertz_params_minimize[e], t_vec, vec)
        pl.plot(t_vec, residual_smooth_gompertz + vec, 'blue', linestyle = '--', linewidth = 1)

    pl.plot(test[e],np.log(test2[e]), 'k+', markersize = 8,markeredgewidth = 2, label = 'Data')
    pl.legend(fontsize = 10)
    pl.xlabel('Time(Hours)', fontsize = 10)
    pl.ylabel('Population(log)', fontsize = 10)
    pl.ticklabel_format(style='scientific', scilimits=[0,3])
    pl.show()
