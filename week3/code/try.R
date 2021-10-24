#try() used to catch an error but lets you keep going
## Runs a simulation that involves sampling from a synthetic population with replacement
## then takes the mean but only if at least 30 unique samples are obtained

doit<-function(x){
  temp_x<-sample(x,replace=TRUE) #take a sample of x
  if(length(unique(temp_x))>30) {#only take mean if sample was sufficent, more than 30
      print(paste("Mean of this sample was:", as.character(mean(temp_x))))
      }
  else {
      stop("Couldn't calculate mean: too few unique values!")
      }
}
# stop() stops exectuion and executes and error action
# sample(x,size,replace) takes a sample of the specified size from x,
## should sampling be with replacement?

set.seed(1345)
popn<-rnorm(50)
hist(popn)

#run the function on this population 15 times using vectorization(lapply)
#lapply(1:15,function(i) doit(popn)) #function(i) is a placeholder
#ERRORR!!!! too little unique sample

#try() supressess the error bug and allows result output 
result<-lapply(1:15,function(i) try(doit(popn),FALSE))

class(result)
result #running this, you can see the store run output 

#Storing results manually in a loop
result<-vector("list",15) #preallocating a loop of 15
for (i in 1:15){
  result[[i]]<-try(doit(popn), FALSE)
  }



