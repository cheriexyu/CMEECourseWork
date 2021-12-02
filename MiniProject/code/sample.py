#!/usr/bin/env python3
#############################
# Sample and Graphing
#############################
#Sampling Gompertz Equation
from lmfit import Minimizer, Parameters, report_fit
import pandas as pd
import scipy as sc
from scipy import stats 
from scipy.stats import linregress
import numpy as np
import matplotlib.pylab as pl 
import seaborn as sns 
import csv

data = pd.read_csv("../data/editeddata.csv")
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
test.to_csv("../data/data_after_sample_gompertz.csv",sep=",",quoting=csv.QUOTE_ALL) #save as csv to edited data after sampling gompertz, NEED TO EDIT THIS

outpop_test = test["outpop"].to_numpy()
outtime_test = test["outtime"].to_numpy()
ID = test["ID"].to_numpy()

#######SAMPLE
slope_r_max=[]
diff_lag=[]

#gompertz_minimize = []
#gompertz_residuals = [] #all these are 27500
params = [] #all these are 27500
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
                #gompertz_residuals.append(fit_gompertz_NLLS.residual)
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
                #gompertz_residuals.append(text)
                #gompertz_params_minimize.append(text)
    
        except Exception:
            print(f"This didn't work; d = {d}") # DID not work for subset 280 to 284 
    

df2 = pd.DataFrame(alloc) #save parameters and AIC to csv 
df2.columns = ['N_0', 'N_max','r_max','t_lag','AIC'] 
df2.insert(0, 'ID', ID)
df2.set_index('ID', inplace=True)

df2
df2=df2.round(3)
df2.to_csv("../data/minimized_paras_gompertz.csv", sep=',',na_rep="NaN")


########################################################################################################################################################

#Plot all graphs into graphs folder

minimized = pd.read_csv("../data/minimized_paras_gompertz.csv")
minimized_array = minimized[["N_0", "N_max", "r_max","t_lag"]].to_numpy() #minimised_gompertz parameters

#####Cubic Equation
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

for d in range(len(outtime_test)):
    if len(outtime_test[d])>4:
        minner = Minimizer(residuals_linear, params_linear, fcn_args=(outtime_test[d],np.log(outpop_test[d])))
        fit_linear_NLLS = minner.minimize()
        linear_minimize.append(fit_linear_NLLS)
        linear_residuals.append(fit_linear_NLLS.residual)
        linear_params.append(fit_linear_NLLS.params)
        AIC.append(fit_linear_NLLS.aic)
    else:
        text = np.nan
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

for d in range(len(outtime_test)):
    if len(outtime_test[d])>3:
        minner_quadratic = Minimizer(residuals_quadratic, params_quadratic, fcn_args=(outtime_test[d],np.log(outpop_test[d])))
        fit_quadratic_NLLS = minner_quadratic.minimize()
        quadratic_minimize.append(fit_quadratic_NLLS)
        quadratic_residuals.append(fit_quadratic_NLLS.residual)
        quadratic_params.append(fit_quadratic_NLLS.params)
        AIC_quadratic.append(fit_quadratic_NLLS.aic)
    else:
        text = np.nan
        quadratic_minimize.append(text)
        quadratic_residuals.append(text)
        quadratic_params.append(text)
        AIC_quadratic.append(text)

###### Gompertz
def residuals_gompertz(params, t, data):
    v = params.valuesdict()
    model = v['N_0'] + (v['N_max'] - v['N_0']) * np.exp(-np.exp(v['r_max'] * np.exp(1) * (v['t_lag'] - t) / ((v['N_max'] - v['N_0']) * np.log(10)) + 1))
    return model - data


gompertz_minimize = []
gompertz_residuals = [] #all these are 27500
gompertz_params = [] #all these are 27500
params = []
for d in range(len(outtime_test)):    
    params_gompertz=Parameters()
    params_gompertz.add_many(('N_0', minimized_array[d][0] , True, None, None, None, None),('N_max', minimized_array[d][1] , True, None, None, None, None),('r_max', minimized_array[d][2], True, None, None, None, None),('t_lag', minimized_array[d][3], True, None, None, None, None)) 
    params.append(params_gompertz)

    if len(outtime_test[d])>4:
        minner_gompertz = Minimizer(residuals_gompertz, params[d], fcn_args=(outtime_test[d],np.log(outpop_test[d])))
        fit_gompertz_NLLS = minner_gompertz.minimize() 
        gompertz_minimize.append(fit_gompertz_NLLS)
        gompertz_residuals.append(fit_gompertz_NLLS.residual)
        gompertz_params.append(fit_gompertz_NLLS.params)
    else:
        text = np.nan
        gompertz_minimize.append(fit_gompertz_NLLS)
        gompertz_residuals.append(fit_gompertz_NLLS.residual)
        gompertz_params.append(fit_quadratic_NLLS.params)

###### AIC Output
AIC_output = pd.DataFrame(ID,columns=['ID'])
AIC_output['Cubic'] = AIC
AIC_output['Quadratic'] = AIC_quadratic

AIC_gompertz_csv = pd.read_csv("../data/minimized_paras_gompertz.csv")
AIC_gompertz = AIC_gompertz_csv["AIC"].to_numpy()
AIC_output['Gompertz'] = AIC_gompertz
AIC_output.set_index('ID', inplace=True)

AIC_output.to_csv("../data/AIC_output.csv",sep=',',na_rep="NA")

####GRAPHING

for e in range(len(outpop_test)): #Cubic
    f1 = pl.figure()
    if len(outtime_test[e])>4:
        result = np.log(outpop_test[e]) + linear_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
        pl.plot(outtime_test[e], result , 'g.', markersize = 8, label = 'Cubic') #plots the datapoints from above
        t_vec=np.linspace(0,max(outtime_test[e])+10,1000) #to get a smooth curve we need to plug in our own time vector (x)
        vec=np.ones(len(t_vec)) 
        smooth_line = residuals_linear(linear_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
        pl.plot(t_vec,smooth_line + vec, 'green', linestyle = '--', linewidth = 1) #plot the smooth curve  

    if len(outtime_test[e])>3: #Quadratic
        result_quadratic = np.log(outpop_test[e]) + quadratic_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
        pl.plot(outtime_test[e], result_quadratic , 'y.', markersize = 8, label = 'Quadratic') #plots the datapoints from above
        t_vec=np.linspace(0,max(outtime_test[e])+10,1000) #to get a smooth curve we need to plug in our own time vector (x)
        vec=np.ones(len(t_vec)) 
        smooth_line_quadratic = residuals_quadratic(quadratic_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
        pl.plot(t_vec,smooth_line_quadratic + vec, 'orange', linestyle = '--', linewidth = 1) #plot the smooth curve  


    if len(outtime_test[e])>4: #Gompertz
        result_gompertz = np.log(outpop_test[e]) + gompertz_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
        pl.plot(outtime_test[e], result_gompertz , 'b.', markersize = 8, label = 'Gompertz') #plots the datapoints from above
        t_vec=np.linspace(0,max(outtime_test[e])+10,1000) #to get a smooth curve we need to plug in our own time vector (x)
        vec=np.ones(len(t_vec)) 
        smooth_line_gompertz = residuals_gompertz(gompertz_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
        pl.plot(t_vec,smooth_line_gompertz + vec, 'blue', linestyle = '--', linewidth = 1) #plot the smooth curve  


    pl.plot(outtime_test[e],np.log(outpop_test[e]), 'k+', markersize = 8,markeredgewidth = 2, label = 'Data %i' %ID[e])
    pl.legend(fontsize = 10)
    pl.xlabel('Time(Hours)', fontsize = 10)
    pl.ylabel('Population(log)', fontsize = 10)
    pl.ticklabel_format(style='scientific', scilimits=[0,3])
    #pl.show()
    f1.savefig('./graphs/graph%i.pdf' %ID[e]) 
