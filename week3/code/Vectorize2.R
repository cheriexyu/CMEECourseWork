# Runs the stochastic Ricker equation with gaussian fluctuations (thermal fluctuations)

rm(list = ls())

stochrick <- function(p0 = runif(1000, .5, 1.5), r = 1.2, K = 1, sigma = 0.2,numyears = 100)
{
#run if = generate 1000 random numbers 
  N <- matrix(NA, numyears, length(p0))  #initialize empty matrix

  N[1, ] <- p0 #In row 1 p0 and all the columns of the empty matrix row is year, column is population

 for (pop in 1:length(p0)) { #loop through the populations

    for (yr in 2:numyears){ #for each pop, loop through the years

      N[yr, pop] <- N[yr-1, pop] * exp(r * (1 - N[yr - 1, pop] / K) + rnorm(1, 0, sigma)) # add one fluctuation from normal distribution
    
     }
  
  }
 return(N)
}
view(stochrick())

# Now write another function called stochrickvect that vectorizes the above to
# the extent possible, with improved performance: 
rm(list = ls())

stochrick1 <- function(p0 = runif(1000, .5, 1.5), r = 1.2, K = 1, sigma = 0.2,numyears = 100)
{
N <- matrix(NA, numyears, length(p0))  #initialize empty matrix
N[1, ] <- p0 #In row 1 p0 and all the columns of the empty matrix row is year, column is population
  for (yr in 2:numyears){ #for each pop, loop through the years
    N[yr, (1:length(p0))] <- N[yr-1, (1:length(p0))] * exp(r * (1 - N[yr - 1, (1:length(p0))] / K) + rnorm(1, 0, sigma)) # add one fluctuation from normal distribution
    } #Changed to length of population instead of the first population 
  return(N)
}


view(stochrick1())


#adding fluctuation to every timestep value, add fluctuations in a vectorized way, 
#instead of doing it by column first then every row in two loops
#delete one loop and use apply functions


# print("Vectorized Stochastic Ricker takes:")
# print(system.time(res2<-stochrickvect()))