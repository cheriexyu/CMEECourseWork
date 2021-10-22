######### Functions ##########

## A function to take a sample of size n from a population "popn" and return its mean
myexperiment<-function(popn,n){
  pop_sample<-sample(popn, n, replace=FALSE) #sample() takes a sample of the specified size from the element x (popn),using either with or without replacement 
  return(mean(pop_sample)) #return the mean of that sample taken
}

##Calculate means using a FOR loop on a vector without preallocation:
#write the mean of n in the empty vector by concatenating and looping
loopy_sample1<-function(popn, n, num){ 
  result1<-vector() #Initialize empty vector of size 1 
  for(i in 1:num){ #between range 1 to num
    result1<-c(result1,myexperiment(popn, n)) #concatenate vector,with the calculate mean function
  }
  return(result1)
}

## To run "num" iterations of the experiment using a FOR loop on a vector with preallocation:
loopy_sample2<-function(popn, n, num){
  result2<-vector(,num) #preallocate expected size
  for(i in 1:num){
    result2[i]<-myexperiment(popn,n) #calculate mean function of size n and set it as i and puts it into the vector
    #then loops and continues on from i (1 to 2)
  }
  return(result2)
}

## To run "num" iterations of the experiment using a For loop on a loop with preallocations:
loopy_sample3<-function(popn, n, num){
  result3<-vector("list", num) #preallocate expected size
  for(i in 1:num){ 
    result3[[i]]<-myexperiment(popn, n) #mean, put it as i and put it into the vector 
  }
  return(result3)
}

## To run "num" iterations of the experiment using vectorization with lapply:
lapply_sample<-function(popn, n,num){ 
  result4<-lapply(1:num, function(i) myexperiment(popn, n)) #lapply num, with the function i 
}  #function(i) does not mean anything, just a placeholder to tell to do that function to all from 1:num


## To run "num" iterations fo the experiment using vectorization with sapply:
sapply_sample<-function(popn, n, num){
  result5<-sapply(1:num, function(i) myexperiment(popn, n))
  return(result5)
}

#Generate population
set.seed(12345)
popn<-rnorm(1000) #Generate population
hist(popn)

#Run and time the different functions
n<-100 #sample size for each experiment
num<-10000 #Number of times to rerun the experiment

print("Using loops without preallocation on a vector took:")
print(system.time(loopy_sample1(popn,1000,650)))

print("Using loops with preallocation on a vector took:")
print(system.time(loopy_sample2(popn,1000,650)))

print("Using loops with preallocation on a list took:")
print(system.time(loopy_sample3(popn,1000,650)))

print("Using the vectorized sapply function (on a list) took:")
print(system.time(sapply_sample(popn,1000,650)))

print("Using the vectorized lapply fuction (on a list) took:")
print(system.time(lapply_sample(popn,1000,650)))

#Using loops without preallocation is usually the slowest