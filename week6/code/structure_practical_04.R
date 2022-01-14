
# Practical on population structure from genomic data of turtles

### Read genotype data (as binary matrix, like done for the killer whale data)
len <- 2000
data <- as.matrix(..., colClasses=rep("numeric", len) ...)
dim(data)

### you may wish to assign an name (A,B,C,D) for each location; create a variable that contains this information
locations <- .... # hint: use "rep", type ?rep for help

## 1) Population subdivision

### To test whether there is population subdivision we can do several things
# A: build a tree, B: do a PCA, C: calculate FST
# pick one, here some suggestions for the related code with functions to use

# option A:
### we can build a tree of all samples and check whether we observe some cluster
### we can do this by first constructing a genetic distance matrix and then a tree
# genetic distance: https://en.wikipedia.org/wiki/Genetic_distance

# to calculate a distance matrix, use "dist" type ?dist
...

# then a tree can be obtained using "hclust" from the distance matrix, type ?hclust
...

# finally plot the tree
plot(..., labels=locations)

## option B:
### alternatively we can do a PCA (principal component analysis)
# https://en.wikipedia.org/wiki/Principal_component_analysis

# for visualisation, we can assign a vector of colors for each location
colors <- ... # again you may use "rep"

### also, it's good practice to filter our (remove) low-frequency variants (SNPs with low frequency) before doing a PCA since they don't carry important information on the structure

# calculate allele frequency using code from yesterday
...
# keep only sites (columns) if the allele frequency is larger than 0.05 (5%)
...

# a PCA can be done in R using "prcomp" function, type ?prcomp
pca <- prcomp(..., center=T, scale=T)

# have a look at the results
summary(pca)

# the coordinates for the components are in pca$x
pca$x

# you can plot the first component (on x-axis) vs the second one (on y-axis), for instance
plot(..., col=colors, pch=1)
# add a legend to the plot with "legend"
legend(...)


## option C:
### we can calculate FST between locations from haplotype

# read the haplotype (not genotype!) data 
data2 <- as.matrix(read.csv(... colClasses=rep("numeric", len)))

# again we can simply remove SNPs with low frequency, keep only sites/columns where the allele frequency is greater than 0.05 (5%)
...


# this function calculates FST given two binary matrices in input 
calcFST <- function(pop1, pop2) {

	# warning: this works only for equal sample sizes! don not use for your own research!

	fA1 <- as.numeric(apply(FUN=sum, X=pop1, MAR=2)/nrow(pop1))
	fA2 <- as.numeric(apply(FUN=sum, X=pop2, MAR=2)/nrow(pop2))

	FST <- rep(NA, length(fA1))

	for (i in 1:length(FST)) {

		HT <- 2 * ( (fA1[i] + fA2[i]) / 2 ) * (1 - ((fA1[i] + fA2[i]) / 2) )
		HS <- fA1[i] * (1 - fA1[i]) + fA2[i] * (1 - fA2[i]) 

		FST[i] <- (HT - HS) / HT

	}
	FST
}

# usage:
# calcFST(data_pop1, data_pop2) -> it will return a value of FST each for SNP

# how can you split the data into various populations?

# you may wish to summarise the vector of FST values either using a plot or by calculating its average avlue
...

### do these values indicate a certain degree of population subdivision?

## 2) do these values provide evidence of isolation by distance or not? why?



