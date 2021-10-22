#applying the same function to row/colums of a matrix using apply

##Build a random matrix
M<-matrix(rnorm(100),10,10) #with a set of number of a normal distribution, in a 10x10 matrix

##Take the mean of each row
RowMeans<-apply(M,1,mean) #apply function apply(matrixorarray, margin=1,fun)
#margin 1 = rows, 2 = columns 
#fun = function to apply
print(RowMeans)

##Now the variance
RowVars<-apply(M,1,var)
print(RowVars)

##By column
ColMeans<-apply(M,2,mean)
print(ColMeans)
