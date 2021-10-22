a <- 4
a
a * a #Multipilcation
a_squared <- a*a
a_squared
sqrt(a_squared)

#building a vector with c(concatenating)
v <- c(0,1,2,3,4)
v
is.vector(v) #True or false statement 

var(v) #variance
median(v) #median
sum(v) #sum of all elements
prod(v + 1) #multiplication
length(v) #how many elements in the vector

li = list(c(1,2,3))
class(li)

v <- TRUE #Boolean variables
v
class(v) #logical same as boolean variables

v <- 3.2 #numeric
class(v)
v <- 2L #integer
class(v)
v <- "A string"
class(v) #string
b <- NA
class(b) #logical

is.NA(b)
b <-  0/0
b

as.logical(5) #R always put 0 as False and others as True


#Vectors
a <- 5
is.vector(a)

v1 <- c(0.02,0.5,1)
v2 <- c("a", "bc", "def", "ghij")
v3 <- c(TRUE,TRUE,FALSE)
v1
v1;v2;v3
v1 <- c(0.02, TRUE, 1) #R vectors only store data of a single type so unlike
# here, R will try to homogenize all the data to the same type
v1

#Matrix
mat1 <- matrix(1:25,5,5)
mat1
mat1 <- matrix(1:25,5,5, byrow=TRUE)
mat1
dim(mat1)

#Arrays
arr1 <- array(1:50, c(5,5,2)) #array from 1 to 50, an array with 5 rows, 
#5 columns and 2 tables 
arr1
arr1[,,1]#show table 1 of arr1
arr1[,,2]#show table 2 of arr1

#Dataframes
Col1<-1:10
Col1
Col2<-LETTERS[1:10]
Col3<-runif(10)  # 10 random numbers from a uniform distribution
Col3
MyDF<-data.frame(Col1,Col2,Col3) #Combine into a dataframe
MyDF
names(MyDF) <- c("MyFirstColumn","My SecondColumn","My.Third.Column") #Changing names 
MyDF
MyDF$MyFirstColumn #Show first column
MyDF$My SecondColumn #ERROR with blank space
colnames(MyDF) #Replacing name , colnames=column names
colnames(MyDF)[2]<-"MySecondColumn" #R starts from 1 unlike python
MyDF

MyDF[,1] #show 1st column 
MyDF[c("MyFirstColumn","My.Third.Column")] #show the two specific column only 
class(MyDF)
str(MyDF) #structure of a dataframe
head(MyDF) #print the top rows and columns
tail(MyDF) #print the bottom rows 

#LISTS
MyList <- list(species=c("Qercus robur", "Fraxinus excelsior"), age=c(123,84))
MyList 
MyList[[1]]
MyList[[2]]
MyList[[1]][1] #To get the first in species
MyList$species #Better method
MyList$age
MyList$species[1] #To get the first in species

pop1<-list(species='Cancer magister',latitude=48.3,longitude=-123.1,startyr=1980,
           endyr=1985, pop=c(303,402,101,607,802,35))
pop1

#Building list of lists
pop1<-list(lat=19,long=57,pop=c(100,101,99)) 
pop2<-list(lat=56,long=-120,pop=c(1,4,7,7,2,1,2))
pop3<-list(lat=32,long=-10,pop=c(12,11,2,1,14))
pops<-list(sp1=pop1,sp2=pop2,sp3=pop3)
pops 
pops$sp1 #check out species 1 = pop1

pops$sp1["pop"] #check out pop1, pop 

#All of these below are the same
pops$sp2["lat"] #check out pop2, lat
pops[[2]]$lat
pops[[2]][1]

pops[[3]]$pop[3]<-102 #Change in sp3, pop3[pop], the 3 integer "2" to "102"
pop3
pops

#Data Frames VS Matrix 
MyMat = matrix(1:8,4,4)
MyMat

MyDF = as.data.frame(MyMat)#Function to return as data frame 
MyDF

object.size(MyMat)
object.size(MyDF) #Checking memory usage of matrix and data frames
#Dataframes have higher memory usage 

#Creating Sequences
years <- 1990:2009 #show sequences in between 
years
years <- 2009:1990 #Show sequences in reverse order
years
seq(1,10,0.5) #Creating sequences with float numbers need 'seq'

#Accessing data structures
MyVar<-c('a','b','c','d','e')
MyVar[1] #start from 1
MyVar[c(3,2,1)] #can be used to set values in different orders
MyVar[c(1,1,5,5)] #repeat indicies

v<-c(0,1,2,3,4) #create a vector named v
v[3]
v[1:3] #get between 1 to 3
v[-3] #remove elements (2)
v[c(1,4)] #access non sequential sequences, output 0 and 3

mat1<- matrix(1:25, 5, 5, byrow=TRUE) #create a new matrix
mat1
mat1[1,2] # [row , column]
mat1[3,4] 
mat1[1,2:4] # list out row 1, columns 2,3,4
mat1[1:2,2:4]
mat1[1,] #get all values from row 1

#Recycling
a <- c(1,5) + 2
a
x <- c(1,2); y<- c(5,3,9,2)
x;y
x+y #because x is shorter than y, it could not be summed, so R repeated x twice 
x + c(y,1) #error msg as R is not comfortable at recycling

#Vector matrix operations
v<-c(0,1,2,3,4)
v2<-v*2 #multiply whole vector by 2
v2
v*v2 #element wise product
t(v)#transpose vector, flip the rows and columns 
v %% t(v) #matrix/vector product 
v3<-1:7 
v3
v4<-c(v2,v3) #concatenate vectors
v4

#Strings and Pasting 
species.name<-"Quercus robur"
species.name
paste("Quercus","robur") #combining the two strings
paste("Quercus", "robur", sep="") #get rid of space
paste("Quercus", "robur", sep=",") #insert comma to seperate
paste('Year is:', 1990:2000) #pasting works in vector

#Seeding number generators
set.seed(1234567)
rnorm(1)
rnorm(10)
set.seed(1234567)
rnorm(11)

#Importing data
MyData<-read.csv("../data/trees.csv")
ls()
head(MyData)
class(MyData)
str(MyData)

write.csv(MyData,"../results/MyData.csv") #Creating a new csv file in results
dir("../results/") #check result directory 
write.table(MyData[1,],file="../results/MyData.csv",append=TRUE) #appending MyData file with new table
write.csv(MyData,"../results/MyData.csv", row.names=TRUE) #write row names from trees into MyData file
write.table(MyData,"../results/MyData.csv", col.names=FALSE) #ignore columne names MyData file
head("../results/MyData.csv")






