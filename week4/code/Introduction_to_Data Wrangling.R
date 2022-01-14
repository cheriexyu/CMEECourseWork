#Directories#
getwd()
setwd("~/Library/Mobile Documents/com~apple~CloudDocs/Imperial/Teaching/PG/Biological Computing in R/20:21/3. Thursday")
list.files()

##Dependencies##
library(dplyr)
library(tidyr)

#Gather#
speciesdiversity <- read.csv("speciesdiversity.csv")
long<-pivot_longer(speciesdiversity, names_to = "Year", values_to = "SpDiv", cols=SpDiv.1991:SpDiv.1992)

long<-pivot_longer(speciesdiversity, names_to = "Year", values_to = "SpDiv", cols=c("SpDiv.1991", "SpDiv.1992"))

##Useful arguments: names_prefix="SpDiv." and values_drop_na=TRUE or FALSE 

long<-pivot_longer(speciesdiversity, names_to = "Year", values_to = "SpDiv", 
                   cols=SpDiv.1991:SpDiv.1992, names_prefix = "SpDiv.")

#Spread#
wide<- pivot_wider(long, names_from = "Year",values_from="SpDiv")

fertility<- read.csv("fertility.csv")

##Arrange##
  #Arrange1#
  arr1 <- arrange(fertility, Age)
  head(arr1)
  tail(arr1)
  #Arrange 2#
  arr2 <- arrange(fertility, desc(Age))
head(arr2)
  
##Select##
  #Select 1#
  sel1<- select(fertility, Age, FSH, Oocytes, Embryos)
  #Select 2#
  sel2<- select(fertility, Age:MeanAFC)
  #Select 3#
  sel3 <- select(fertility, -FSH)
  #Select 4#
  sel4<- select(fertility, contains("AFC"))

##Filter##
  #Filter 1#
  fil1<- filter(fertility, Age<=30&MeanAFC>20)

##Mutate##
  #Mutate 1#
  mut1 <- mutate(fertility, ratio=Embryos/Oocytes)
  str(mut1)
  
##Summarise##
  sum1 <- summarise(fertility, min.FSH = min(FSH), max.FSH =max(FSH))

##Pipe Operator##
  pip1<- fertility%>%filter(Age<=30)%>%select(Age:MeanAFC)

##group_by##
  groups <- group_by(fertility, AgeGroup)
  
##group_by+summarise##
  group_summary <- fertility%>%group_by(AgeGroup)%>%summarise(mean.FSH=mean(FSH), sd.FSH=sd(FSH))

groups<- fertility%>%filter(Age<=40)%>%select(Age:FSH)%>%group_by(AgeGroup)%>%summarise(mean.FSH=mean(FSH), sd.FSH=sd(FSH))
  
    