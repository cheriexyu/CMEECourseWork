#!/usr/bin/env python3
#############################
# LOOP FOR ALL Quadratic and Cubic
#############################
data = pd.read_csv("../../data/data_after_sample_gompertz.csv")
#print("Loaded {} columns.".format(len(data.columns.values))) #load 10 columns
data = data.drop(columns=['Unnamed: 0'])
outpop_test = test["outpop"].to_numpy()
len(outpop_test)
outtime_test = test["outtime"].to_numpy()
ID = test["ID"].to_numpy()

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

for d in range(len(outtime_test)):
    if len(outtime_test[d])>3:
        minner_quadratic = Minimizer(residuals_quadratic, params_quadratic, fcn_args=(outtime_test[d],np.log(outpop_test[d])))
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

#AIC number output to output CSV
AIC_output = pd.DataFrame(ID,columns=['ID'])
AIC_output['Cubic'] = AIC
AIC_output['Quadratic'] = AIC_quadratic

AIC_gompertz_csv = pd.read_csv("../../data/minimized_paras_gompertz.csv")
AIC_gompertz = AIC_gompertz_csv["AIC"].to_numpy()
AIC_output['Gompertz'] = AIC_gompertz
AIC_output.set_index('ID', inplace=True)


AIC_output.to_csv("../../data/AIC_output.csv",sep=',',na_rep="NA")


####GRAPHING

# for e in range(len(outpop)): #Cubic
#     if len(outtime[e])>4:
#         result = np.log(outpop[e]) + linear_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
#         pl.plot(outtime[e], result , 'g.', markersize = 8, label = 'Cubic') #plots the datapoints from above
#         t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector (x)
#         vec=np.ones(len(t_vec)) 
#         smooth_line = residuals_linear(linear_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
#         pl.plot(t_vec,smooth_line + vec, 'green', linestyle = '--', linewidth = 1) #plot the smooth curve  

#     if len(outtime[e])>3: #Quadratic
#         result_quadratic = np.log(outpop[e]) + quadratic_residuals[e] # Make a variable that adds the y datapoints and residuals of the fitted data together, the datapoint on the fitted line 
#         pl.plot(outtime[e], result_quadratic , 'y.', markersize = 8, label = 'Quadratic') #plots the datapoints from above
#         t_vec=np.linspace(0,700,1000) #to get a smooth curve we need to plug in our own time vector (x)
#         vec=np.ones(len(t_vec)) 
#         smooth_line_quadratic = residuals_quadratic(quadratic_params[e],t_vec,vec) #to get a smooth curve we are also getting data points for (y). Plugging in the paramaters using the x (t_vec_), plug in the new data into vec
#         pl.plot(t_vec,smooth_line_quadratic + vec, 'orange', linestyle = '--', linewidth = 1) #plot the smooth curve  

#     pl.plot(outtime[e],np.log(outpop[e]), 'k+', markersize = 8,markeredgewidth = 2, label = 'Data')
#     pl.legend(fontsize = 10)
#     pl.xlabel('Time(Hours)', fontsize = 10)
#     pl.ylabel('Population(log)', fontsize = 10)
#     pl.ticklabel_format(style='scientific', scilimits=[0,3])
#     pl.show(block=False)