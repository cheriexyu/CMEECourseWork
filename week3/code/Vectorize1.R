#Sums all elements of a matrix
#Summary:
#Vectorization are faster and quicker than loops, however if you do want to use loops
#then optimize the code for faster running time. 

M<-matrix(runif(1000000),1000,1000)#1000000 random uniformed numbers in a 1000x1000 matrix

SumALLElements<-function(M){ #Find all the sum
  Dimensions<-dim(M) #show the dimension of M
  Tot<-0
  for (i in 1:Dimensions[1]){ #Calculate the row
    for (j in 1:Dimensions[2]){ #Calculate the column
      Tot<-Tot+M[i,j] #Calculate the sum 
    }
  }
  return(Tot)
}

print("Using loops, the time taken is:")
print(system.time(SumALLElements(M)))

print("Using the in-build vectorized function, the time taken is:")
print(system.time(sum(M)))
