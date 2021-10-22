#Using apply on my own defined function
#function will mutiply the sum by 100 only if 
SomeOperation<-function(v){ 
  if (sum(v) > 0){ #sum(v) is a single value, if the sum of all values in first row of matrix is bigger than 0
    return (v*100) #return sum multiply by 100
  }
    return (v) #if not return v
}

M<-matrix(rnorm(100),10,10)
print(M)
print(apply(M,1,SomeOperation))

