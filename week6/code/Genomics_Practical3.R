## Practical on coalescence theory

## first thing, read genomic data for each population
## since the alleles are encoded as 0 and 1 in this case, it's better to store the data as a matrix


# set the length of the region
len <- 50000

# read data from North
data_N <- as.matrix(read.csv(...)) # reuse previous codes
dim(...) # check for dimensions
