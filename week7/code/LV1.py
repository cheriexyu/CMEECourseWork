#!/usr/bin/env python3
#############################
# Practical 
#############################
"""Self-standing script that plots two graphs of the Lotka-Volterra model in results folder""""

import scipy as sc
import numpy as np
import matplotlib.pylab as p
import scipy.integrate as integrate

#######The Lotka-Volterra model

def dCR_dt(pops,t=0): # Define a new function
    """function that returns the growth rate of consumer and resource population at a given time"""
    R = pops[0]
    C = pops[1]
    dRdt = r * R - a * R * C
    dCdt = -z * C + e * a * R * C
    return np.array([dRdt,dCdt])

#assign parameter values
r = 1.
a = 0.1
z = 1.5
e = 0.75

t=np.linspace(0,15,1000) # generate 1000 evenly spaced numbers from 0 to 50 
t

R0 = 10 #initial conditions for the two population , 10 resources
C0 = 5 #initial conditions for the two population , 5 consumers per unit area 
RC0 = np.array([R0, C0]) #convert to array because dCR_dt function takes in array 

#Create the main argument to input into function
pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True) #infodict returns a modifiable information dictionary object
pops #Now contains the result of the population trajectories 
infodict['message'] #was the intergration sucessful?

#Plot graph
import matplotlib.pylab as p
f1 = p.figure() #Open an empty figure
p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot, [:,0] is all rows, first column
p.plot(t, pops[:,1]  , 'b-', label='Consumer density') #plot [:,1] all rows, second column 
p.grid() #grid in the background
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')

f1.savefig('../results/LV_model.pdf') #save as pdf

###### Graph 2
f2=p.figure()
p.plot(pops[:,0],pops[:,1],'r-')
p.grid() 
p.xlabel('Resource density')
p.ylabel('Consumer density')
p.title('Consumer-Resource population dynamics')

f2.savefig('../results/LV_model2.pdf') #save as pdf
