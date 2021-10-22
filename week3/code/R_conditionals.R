#Functions with conditions

#Check if an integer is even
is.even<-function(n=2){  #write n is 2 if value is not defined 
  if(n%%2==0) #if the module remainder is 0, means its even
  {
    return(paste(n,'is even!')) #paste it is even
  }
  return(paste(n,'is odd!')) #if not paste it is odd
}

is.even(6)

#Check is a number is a power of 2
is.power2<-function(n=2){ #write = 2 if n is not defined 
  if (log2(n) %% 1==0) #if the module R is 0, that means it is the power of 2
  {
    return(paste(n,'is a power of 2!'))
  }
  return(paste(n,'is not a power of 2!'))
}

is.power2(4)

#Checks if a number is prime
is.prime<-function(n){
  if (n==0){ #if n is a 0
    return(paste(n,'is a zero!'))
  }
  if (n==1){ #if n is 1
    return(paste(n,'is just a unit!'))
  }
  ints<-2:(n-1) #
  if (all(n%%ints!=0)){
    return(paste(n,'is a prime!')) 
  }
  return(paste(n,'is a composite!')) #if not any, prime 1 or 0
}

is.prime(3)