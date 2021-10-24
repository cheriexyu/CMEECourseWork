################################################################
################## Wrangling the Pound Hill Dataset ############
################################################################

############# Load the dataset ###############
# header = false because the raw data don't have real headers
MyData <- as.matrix(read.csv("../data/PoundHillData.csv", header = FALSE))

# header = true because we do have metadata headers
MyMetaData <- read.csv("../data/PoundHillMetaData.csv", header = TRUE, sep = ";")
require(tidyverse)
############# Inspect the dataset ###############
head(MyData)
tibble::as_tibble(MyData)
dplyr::glimpse(MyData)

############# Transpose ###############
# To get those species into columns and treatments into rows
tidyr::gather(MyData)

MyData <- t(MyData) #Flip the columns and rows 
head(MyData)
dim(MyData)

############# Replace species absences with zeros ###############
MyData[MyData == ""] = 0 #" " is absences
head(MyData)
dplyr::mutate(MyData=replace(MyData, MyData == "", 0))

############# Convert raw matrix to data frame ###############

TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F) #stringsAsFactors = F is important!, character should not be coverted to a factor = False
#make a new data frame and get rid of the first column (-1) 
colnames(TempData) <- MyData[1,] # assign column names from original data so 
head(TempData)

############# Convert from wide to long format  ###############
require(tidyverse) # load the reshape2 package

#Melt function takes data in wide format and stacks a set of columns into a single columnn of data
??melt #check out the melt function, convert a object into a molten dataframe
# opposite of melt is dcast(), to switch between long and wide

MyWrangledData <- melt(TempData, id=c("Cultivation", "Block", "Plot", "Quadrat"), variable.name = "Species", value.name = "Count")
MyWrangledData # id is the names that stay the same, value name is name of variable used to store values 

#Convert each column into a factor
MyWrangledData[, "Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])
MyWrangledData[, "Block"] <- as.factor(MyWrangledData[, "Block"])
MyWrangledData[, "Plot"] <- as.factor(MyWrangledData[, "Plot"])
MyWrangledData[, "Quadrat"] <- as.factor(MyWrangledData[, "Quadrat"])

#Convert into a integer 
MyWrangledData[, "Count"] <- as.integer(MyWrangledData[, "Count"])

#You convert into factors or integer becasue if you don't R might assumeyour data as other variables e.g plot 1 is not a integer

str(MyWrangledData)
head(MyWrangledData)
dim(MyWrangledData) #Check dimentions , convert data to a long format

############# Exploring the data (extend the script below)  ###############

MyMetaData #Metadata files describes the data 
MyData[MyData == ""] = 0




