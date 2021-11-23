#!/usr/bin/env python3
#############################
# Data testing model linear 
#############################

#remove negative time and population??
#weighted aic vs normal aic

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
data.head()

#ID_0 = data[data['ID']==0] #How to subset data to only get ID 0 with all columns 
#ID_0 

data_subset=data[['ID','Time','PopBio','Time_units','PopBio_units']] #data_subset is a subset of data with only the variables we need

#Loop to get subsets of data into a dictionary 
subset = data_subset['ID'].unique()
output = {a: data_subset[data_subset['ID'] == a ]for a in subset}

#Convert time and population column for all subset into a numpy array 
outtime = [output[i]['Time'].to_numpy() for i in range(len(output))]
outpop = [output[i]['PopBio'].to_numpy() for i in range(len(output))] 
outtime = np.asarray(outtime, dtype=object)
outpop = np.asarray(outpop, dtype=object)

# #outtime and outpop 
# time_0 = output[0]['Time'].to_numpy()
# popbio_0 = output[0]['PopBio'].to_numpy()

#ID_0 = data_subset[data['ID']== 0]  #getting data for only variables we need 
#ID_0 
# #sns.lmplot(x='Time',y='PopBio',data=ID_0,fit_reg=False) #FOR ID 0 
# #pl.show() #show graph

# #Convert the columns into an array 
#time_0 = ID_0['Time'].to_numpy()
#popbio_0 = ID_0['PopBio'].to_numpy()


##############Fiting a phenomenological linear Cubic Equation using NLLS##############
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

#AIC number output
AIC_output = pd.DataFrame(subset,columns=['ID'])
AIC_output['Cubic'] = AIC
AIC_output.to_csv("../../data/AIC_output.csv",sep=',')

#report_fit(linear_minimize[0]) #use this to see the report of each linear 
#linear_minimize.residual[0]
#minner = Minimizer(residuals_linear, params_linear, fcn_args=(time_0,popbio_0))
#fit_linear_NLLS = minner.minimize()
#report_fit(fit_linear_NLLS)
#print(fit_linear_NLLS.aic)
#extract estimated parameter values in a dictionary then into a list
# par_dict = fit_linear_NLLS.params.valuesdict().values()
# par = np.array(list(par_dict))

#calculate residuals (CORRECT but we don't need this)
#print(par)
#def equation(l):
    #model2 = par[0]*l**3 + par[1]*l**2 + par[2]*l + par[3]
    #return model2
#y = equation(time_0)

#residuals = y - popbio_0
#print(residuals)

#Plot the fitted result (ONE LOOP)
# pl.rcParams['figure.figsize'] = [5, 10] #set up figure enivornment with width and height #NEED TO FIGURE THIS OUT
# result = popbio_0 + fit_linear_NLLS.residual # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
# pl.plot(time_0,result, 'y.', markersize = 10, label = 'Cubic') #plots the datapoints from above

# t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector (x)
# vec=np.ones(len(t_vec)) #allocating a vector of one for the below function
# smooth_line = residuals_linear(fit_linear_NLLS.params,t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec

# pl.plot(t_vec,smooth_line + vec, 'orange', linestyle = '--', linewidth = 1) #plot the smooth curve  
# pl.plot(time_0,popbio_0, 'r+', markersize = 10,markeredgewidth = 2, label = 'Data')

# pl.legend(fontsize = 10)
# pl.xlabel('Time(Hours)', fontsize = 10)
# pl.ylabel('Population', fontsize = 10)
# pl.ticklabel_format(style='scientific', scilimits=[0,3])
# pl.show(block=False)

#Plot FOR LOOP
# pl.rcParams['figure.figsize'] = [5, 10] #set up figure enivornment with width and height #NEED TO FIGURE THIS OUT
# t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector (x)
# vec=np.ones(len(t_vec)) #allocating a vector of one for the below function

# for e in range(len(outpop)):
#     if len(outtime[e])>4:
#         result = np.log(outpop[e]) + linear_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
#         pl.plot(outtime[e], result , 'g.', markersize = 10, label = 'Cubic') #plots the datapoints from above
#         smooth_line = residuals_linear(linear_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
#         pl.plot(t_vec,smooth_line + vec, 'green', linestyle = '--', linewidth = 1) #plot the smooth curve  
#         pl.plot(outtime[e],np.log(outpop[e]), 'r+', markersize = 10,markeredgewidth = 2, label = 'Data')
#         pl.show()


pl.legend(fontsize = 10)
pl.xlabel('Time(Hours)', fontsize = 10)
pl.ylabel('Population', fontsize = 10)
pl.ticklabel_format(style='scientific', scilimits=[0,3])
pl.show(block=False)

#Should I make the axis better? 700 hours mean nothing and should i log the 7 axis?

##############Fiting a phenomenological Quadratic Equation using NLLS##############

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

quadratic_minimize = []
quadratic_residuals = []
quadratic_params = []
AIC_quadratic = [] 

for f in range(len(outtime)):
    if len(outtime[f])>3:
        minner_quadratic = Minimizer(residuals_quadratic, params_quadratic, fcn_args=(outtime[f],np.log(outpop[f])))
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

#AIC number output
AIC_output['Quadratic'] = AIC_quadratic
AIC_output.to_csv("../../data/AIC_output.csv",sep=',')

#Plotting
# pl.rcParams['figure.figsize'] = [5, 10] #set up figure enivornment with width and height #NEED TO FIGURE THIS OUT
# t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector (x)
# vec=np.ones(len(t_vec)) #allocating a vector of one for the below function

# for e in range(len(outpop)):
#     if len(outtime[e])>4:
#         result_quadratic = np.log(outpop[e]) + quadratic_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
#         pl.plot(outtime[e], result_quadratic , 'y.', markersize = 10, label = 'Quadratic') #plots the datapoints from above
#         smooth_line_quadratic = residuals_quadratic(quadratic_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
#         pl.plot(t_vec,smooth_line_quadratic + vec, 'orange', linestyle = '--', linewidth = 1) #plot the smooth curve  
#         pl.plot(outtime[e],np.log(outpop[e]), 'r+', markersize = 10,markeredgewidth = 2, label = 'Data')







##############Fitting the Gompertz Model using NLLS##############

sns.lmplot(x='Time',y='PopBio',data=ID_0,fit_reg=False) #FOR ID 0 
pl.show(block=True)

#FOR first ID
outtime[0]
outpop[0]

#Parameters
params_gompertz=Parameters()
params_gompertz.add_many(('N_0', np.log(outpop[0][-1]) , True, None, None, None, None),
                         ('N_max', np.log(max(outpop[0])) , True, None, None, None, None),
                         ('r_max', 0.00383, True, None, None, None, None),
                         ('t_lag', 334.939759036145, True, None, None, None, None)) #0.0086293 is the correct one via eyeing, 334 was calculated by diff 

np.log(outpop[0][-1]) #N_0, last number of the list is the starting value
np.log(max(outpop[0])) #N_max

#Calculate the slope (max growth rate) as rate of growth r_max
from scipy import stats 
from scipy.stats import linregress
x = outtime[0]
y = np.log(outpop[0])
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) #calc regression line using least square 
slope #0.003827136617541358 

#Calculate the time_lag 
np.diff(np.log(outpop[0])) #Differences between population points 
np.diff(np.diff(np.log(outpop[0]))) #Differences between the Differences 
max(np.diff(np.diff(np.log(outpop[0])))) # Max differences
np.argmax(np.diff(np.diff(np.log(outpop[0])))) #Location 15 = is the location of the max diff of diff in the array
outpop[0][np.argmax(np.diff(np.diff(np.log(outpop[0]))))] #0.197290029683953, number 15 this is the data point of end the exponential growth 
outtime[0][np.argmax(np.diff(np.diff(np.log(outpop[0]))))] #time number when p is 0.197

#Function
def residuals_gompertz(params, t, data):
    v = params.valuesdict()
    model = v['N_0'] + (v['N_max'] - v['N_0']) * np.exp(-np.exp(v['r_max'] * np.exp(1) * (v['t_lag'] - t) / ((v['N_max'] - v['N_0']) * np.log(10)) + 1))
    return model - data 

minner = Minimizer(residuals_gompertz, params_gompertz, fcn_args=(outtime[0], np.log(outpop[0])))
#Perform the minimization
fit_gompertz = minner.minimize()
report_fit(fit_gompertz)

result_gompertz = np.log(outpop[0]) + fit_gompertz.residual
pl.plot(outtime[0], result_gompertz, 'g.', markersize = 10, label = 'Gompertz')
#Get a smooth curve by plugging a time vector to the fitted logistic model
t_vec = np.linspace(0,700,1000)
log_N_vec = np.ones(len(t_vec))
residual_smooth_gompertz = residuals_gompertz(fit_gompertz.params, t_vec, log_N_vec)
pl.plot(t_vec, residual_smooth_gompertz + log_N_vec, 'green', linestyle = '--', linewidth = 1)
pl.plot(outtime[0], np.log(outpop[0]), 'r+', markersize = 10,markeredgewidth = 2, label = 'Data')
pl.show()

####LOOPS for ALL dataset#####

for k in range(len(outpop)):
    x = outtime[k]
    y = np.log(outpop[k])
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y) #calculate slope, r_max
    diff = outtime[k][np.argmax(np.diff(np.diff(np.log(outpop[k]))))] #calculate t_lag
    params_gompertz=Parameters()
    params_gompertz.add_many(('N_0', np.log(outpop[k][-1]) , True, None, None, None, None),('N_max', np.log(max(outpop[k])) , True, None, None, None, None),('r_max', slope, True, None, None, None, None),('t_lag', diff, True, None, None, None, None)) 

#Function
def residuals_gompertz(params, t, data):
    v3 = params.valuesdict()
    model = v3['N_0'] + (v3['N_max'] - v3['N_0']) * np.exp(-np.exp(v3['r_max'] * np.exp(1) * (v3['t_lag'] - t) / ((v3['N_max'] - v3['N_0']) * np.log(10)) + 1))
    return model - data 

gompertz_minimize = []
gompertz_residuals = []
gompertz_params = []
AIC_gompertz = [] 

for m in range(len(outtime)):
    if len(outtime[m])>4:
        minner_gompertz = Minimizer(residuals_gompertz, params_gompertz, fcn_args=(outtime[m],np.log(outpop[m])))
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

AIC_output['Gompertz'] = AIC_gompertz
AIC_output.to_csv("../../data/AIC_output.csv",sep=',')


#Notes
outpop[0][14]
outtime[0][14]

cut_time = outtime[0][16:28] 
cut_pop = outpop[0][16:28] #cut the graph at the end of the exponential graph
np.diff(np.log(cut_pop)) #Differences between population points 
np.diff(np.diff(np.log(cut_pop))) #Differences between the Differences 
max(np.diff(np.diff(np.log(cut_pop)))) # Max differences
np.argmax(np.diff(np.diff(np.log(cut_pop)))) #10 number position in the cut_pop array
cut_time[np.argmax(np.diff(np.diff(np.log(cut_pop))))] #286.74698795


slope = (y2 - y1) / (x2 - x1)
y2= np.log(outpop[0][15])
x2 = outtime[0][15]
y1 = np.log(outpop[0][14])
x1 = outtime[0][14]

x = outtime[0]
y = np.log(outpop[0])
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

output[0] = dataframe

def calc_slope(x):
    slope=np.polyfit(range(len(x)),x,1)[0]
    return slope

new['slope']=new.rolling(60, min_periods=2).apply(calc_slope)

#################### Rolling Regression??

new = pd.DataFrame(output[0]['Time'])
new['PopBio'] = (output[0]['PopBio'])

def get_slope(array):
    y = np.log(array)
    x = np.arange(len(y))
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    return slope

new['roll_slope']=new.PopBio.Rolling(2).apply(get_slope,raw=True)

#.reset_index(0, drop=True)


####################################################################Plotting all graphs####################################################################

pl.rcParams['figure.figsize'] = [5, 10] #set up figure enivornment with width and height #NEED TO FIGURE THIS OUT
t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector (x)
vec=np.ones(len(t_vec)) #allocating a vector of one for the below function

for e in range(len(outpop)): #Quadratic
    if len(outtime[e])>3:
        result_quadratic = outpop[e] + quadratic_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
        pl.plot(outtime[e], result_quadratic , 'y.', markersize = 10, label = 'Quadratic') #plots the datapoints from above
        smooth_line_quadratic = residuals_quadratic(quadratic_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
        pl.plot(t_vec,smooth_line_quadratic + vec, 'orange', linestyle = '--', linewidth = 1) #plot the smooth curve  

for e in range(len(outpop)): #Cubic 
    if len(outtime[e])>4:
        result = np.log(outpop[e]) + linear_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
        pl.plot(outtime[e], result , 'g.', markersize = 10, label = 'Cubic') #plots the datapoints from above
        smooth_line = residuals_linear(linear_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
        pl.plot(t_vec,smooth_line + vec, 'green', linestyle = '--', linewidth = 1) #plot the smooth curve  

for e in range(len(outpop)): #Gompertz 
    if len(outtime[e])>4:
        result_gompertz = np.log(outpop[e]) + gompertz_residuals[e] #Gompertz 
        pl.plot(outtime[e], result_gompertz, 'b.', markersize = 10, label = 'Gompertz') #datapoints
        residual_smooth_gompertz = residuals_gompertz(gompertz_params[e], t_vec, vec)
        pl.plot(t_vec, residual_smooth_gompertz + vec, 'blue', linestyle = '--', linewidth = 1)

pl.plot(outtime[e],np.log(outpop[e]), 'r+', markersize = 10,markeredgewidth = 2, label = 'Data')
pl.legend(fontsize = 10)
pl.xlabel('Time(Hours)', fontsize = 10)
pl.ylabel('Population(log)', fontsize = 10)
pl.ticklabel_format(style='scientific', scilimits=[0,3])
pl.show()


#Plotting all graphs for e = 0
pl.rcParams['figure.figsize'] = [5, 10] #set up figure enivornment with width and height #NEED TO FIGURE THIS OUT
t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector (x)
vec=np.ones(len(t_vec)) #allocating a vector of one for the below function

result_quadratic = np.log(outpop[e]) + quadratic_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
pl.plot(outtime[e], result_quadratic , 'y.', markersize = 10, label = 'Quadratic') #plots the datapoints from above
smooth_line_quadratic = residuals_quadratic(quadratic_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
pl.plot(t_vec,smooth_line_quadratic + vec, 'orange', linestyle = '--', linewidth = 1)

result = np.log(outpop[e]) + linear_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
pl.plot(outtime[e], result , 'g.', markersize = 10, label = 'Cubic') #plots the datapoints from above
smooth_line = residuals_linear(linear_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
pl.plot(t_vec,smooth_line + vec, 'green', linestyle = '--', linewidth = 1)

result_gompertz = np.log(outpop[e]) + gompertz_residuals[e] #Gompertz 
pl.plot(outtime[e], result_gompertz, 'b.', markersize = 10, label = 'Gompertz') #datapoints
residual_smooth_gompertz = residuals_gompertz(gompertz_params[e], t_vec, vec)
pl.plot(t_vec, residual_smooth_gompertz + vec, 'blue', linestyle = '--', linewidth = 1)

pl.plot(outtime[e],np.log(outpop[e]), 'r+', markersize = 10,markeredgewidth = 2, label = 'Data')
pl.legend(fontsize = 10)
pl.xlabel('Time(Hours)', fontsize = 10)
pl.ylabel('Population(log)', fontsize = 10)
pl.ticklabel_format(style='scientific', scilimits=[0,3])
pl.show()


