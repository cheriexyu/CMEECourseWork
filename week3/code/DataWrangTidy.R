################################################################
################## Wrangling the Pound Hill Dataset ############
################################################################
library(tidyverse)
library(dplyr)
library(tidyr)

############# Load the dataset ###############
# header = false because the raw data don't have real headers
MyData <- as.matrix(read.csv("../data/PoundHillData.csv", header = FALSE))

############# Inspect the dataset and Transpose ###############
head(MyData)
MyData<-tibble::as_tibble(data.frame(t(MyData),stringsAsFactors = F)) #convert matrix to dataframe
dplyr::glimpse(MyData)

############# Replace species absences with zeros ###############
MyData<-MyData %>% dplyr::mutate_all(list(~na_if(.,"")))
MyData<-MyData %>% mutate_all(funs(replace(., is.na(.), 0)))
MyData

############# Convert from wide to long format  ###############
MyData<-MyData %>% set_names(slice(.,1)) #Convert first row to column name
MyData<-MyData %>% slice(-1) #Delete duplicated name
view(MyData)

print(MyData[45]) #View last column

EditMyData<-MyData%>%pivot_longer(`Achillea millefolium`:`Vulpia myuros `, names_to = "Species",values_to="Count")
head(EditMyData)

#Convert each column into a factor
EditMyData<-EditMyData%>%mutate_at(1:4,as.factor)

#Convert into a integer 
EditMyData<-EditMyData%>%mutate_at(6,as.integer)
head(EditMyData)

#You convert into factors or integer becasue if you don't R might assumeyour data as other variables e.g plot 1 is not a integer

str(EditMyData)
head(EditMyData)
dim(EditMyData) #Check dimentions 




