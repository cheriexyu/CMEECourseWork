#In loops, memory allocation for a variable that will change during loop is slow
#Making a loop that resizes a vector repeatly makes R slow

NoPreallocFun <- function(x){
  a<-vector() #empty vector
  for (i in 1:x) { #1 to 10
    a<-c(a,i) #concatenate vector and i
    print(a) # a is the previous loop number with the new i 
    print(object.size(a))
  }
}
system.time(NoPreallocFun(10))
#R resize vector and reallocate memory. can get slow as vector gets big

#Reallocating vector that fits all values means R does not need to reallocate memory, so will be faster
PreallocFun <- function(x){
  a <- rep(NA,x) #Pre allocated vector , filled the vector with NA first 
  for (i in 1:x) {
    a[i] <- i
    print(a)
    print(object.size(a))
  }
}

system.time(PreallocFun(10))