#!/usr/bin/env python3
#############################
# AIC rescaling 
#############################
import pandas as pd
import scipy as sc 
import csv
import numpy as np

aic = pd.read_csv("../data/AIC_output.csv")
aic.dropna(axis=0,how ='all',subset=["Quadratic","Cubic","Gompertz"],inplace=True) #drop rows with ALL NA
aic.to_csv("../data/AIC_output.csv",sep=',',na_rep="NA")

cubic_aic = aic["Cubic"].to_numpy(na_value=np.nan)
quadratic_aic = aic["Quadratic"].to_numpy(na_value=np.nan)
gompertz_aic = aic["Gompertz"].to_numpy(na_value=np.nan)
ID_aic = aic["ID"].to_numpy(dtype=object)

sample_size = pd.read_csv("../data/sample_size.csv")
sample_size.sort_values(by=['ID'],inplace=True)
size = sample_size["Sample_Size"].to_numpy() #Array of samples sizes 

aicc = np.ones((273,3)) #273 after dropping all NAs, preallocate vector

###########
#calculate AICc
aicc_cubic = [cubic_aic[m] * ( size[m] / (size[m] - 4 - 1)) for  m in range(len(cubic_aic))] 
aicc_quadratic = [quadratic_aic[m] * ( size[m] / (size[m] - 3 - 1)) for  m in range(len(cubic_aic))]
aicc_gompertz = [gompertz_aic[m] * ( size[m] / (size[m] - 4 - 1)) for  m in range(len(cubic_aic))]

aicc[:,0] = aicc_cubic
aicc[:,1] = aicc_quadratic
aicc[:,2] = aicc_gompertz


aicc_df = pd.DataFrame(aicc,columns=["Cubic","Quadratic","Gompertz"])
aicc_df["ID"] = ID_aic
aicc_df.set_index('ID', inplace=True)

aicc_df.to_csv("../data/AICc_output.csv",sep=',',na_rep="NA") #output AICc as a csv

###########
#∆AIC, Loop through to calculate 

Aicc_min = [min(aicc[n]) for n in range(len(cubic_aic))]

aicc_scaled = np.ones((273,3))
for n in range(len(cubic_aic)):
    """∆AIC"""
    output = aicc[n] - Aicc_min[n]
    aicc_scaled[n] = output

scaled_aicc = pd.DataFrame(aicc_scaled,columns=["Cubic","Quadratic","Gompertz"])
scaled_aicc["ID"] = ID_aic
scaled_aicc.set_index('ID', inplace=True)
scaled_aicc.to_csv("../data/scaled_aicc.csv",sep=',',na_rep="NA")

###########
#Akaike Weights

AICC_weights = np.ones((273,3))
for k in range(len(cubic_aic)):
    """loops over data to calculate akaike weights"""
    value = np.exp( -0.5 * aicc_scaled[k])
    value = value / np.sum(value)
    AICC_weights[k] = value

akaike_weight = pd.DataFrame(AICC_weights,columns=["Cubic","Quadratic","Gompertz"])
akaike_weight["ID"] = ID_aic
akaike_weight.set_index('ID', inplace=True)
akaike_weight.to_csv("../data/akaike_weight.csv",sep=',',na_rep="NA")
