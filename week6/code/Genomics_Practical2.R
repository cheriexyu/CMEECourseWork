### Practical on genetic drift, mutation and divergence

# western
len <- 20000
data_w <- read.csv("../data/western_banded_gecko.csv", stringsAsFactors=F, header=F, colClasses=rep("character", len))
dim(data_w) # it is always good to check the dimensions of your data frame

# bent-toed
data_b <- read.csv("../data/bent-toed_gecko.csv", stringsAsFactors=F, header=F, colClasses=rep("character", len))
dim(data_b)

# leopard
data_l <- read.csv("../data/leopard_gecko.csv", stringsAsFactors=F, header=F, colClasses=rep("character", len))
dim(data_l)