#Opening a matrix
MyData<-as.matrix(read.csv("../data/PoundHillData.csv",header=FALSE))
class(MyData)
MyData
MyMetaData<-read.csv("../data/PoundHillMetaData.csv",header=TRUE, sep=";")
class(MyMetaData)
head(MyMetaData)
MyData <- t(MyData) 
#Refer to DataWrang.R for data wrangling 

#####Opening as a data frame as needed by R for data analysis. 
#Creating a dataframe while excluding the first matrix row as its the column names
TempData<-as.data.frame(MyData[-1,],stringsAsFactors = F)

# Strings as factors is needed because we don't want R to convert columns to factors
head(TempData)
colnames(TempData)<-MyData[1,]
head(TempData) 
#Delete row names, I don't like them
rownames(TempData)<-NULL
head(TempData)

#Convert data to long format
install.packages("reshape2")
library("reshape2")
MyWrangledData<-melt(TempData, id=c("Cultivation","Block","Plot","Quadrat"), variable.name="Species", value.name="Count")
head(MyWrangledData);tail(MyWrangledData) #show the head and tail (5 rows each)

#Convert each column into a factor
MyWrangledData[, "Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])
MyWrangledData[, "Block"] <- as.factor(MyWrangledData[, "Block"])
MyWrangledData[, "Plot"] <- as.factor(MyWrangledData[, "Plot"])
MyWrangledData[, "Quadrat"] <- as.factor(MyWrangledData[, "Quadrat"])

#Convert into a integer 
MyWrangledData[, "Count"] <- as.integer(MyWrangledData[, "Count"])
str(MyWrangledData)

if (!require("tidyverse", character.only=T, quietly=T)) {
  install.packages("tidyverse")
  library("tidyverse", character.only=T)
}
tidyverse_packages(include_self = TRUE)

# "::" allow you to access a particular function from a package 
tibble::as_tibble(MyWrangledData)#Data frames that are lazy surly and do less 

dplyr::glimpse(MyWrangledData) #Change the dataframe to like strings but nicer, to see all the data like print

dplyr::filter(MyWrangledData,Count>100) #subsetting data to only showing rows that satisfy your condition
#here is more than 100

dplyr::slice(MyWrangledData,10:15)

