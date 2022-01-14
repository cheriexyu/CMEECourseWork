data <- read.csv("~/Documents/Bioinformatics/bears.csv",stringsAsFactors=F, header=F, colClasses=rep("character", 10000))
nrow(data)
ncol(data)
dim(data)
#1.identify which positions are SNPs (polymorphic, meaning that they have more than one allele)
#which column is different 
snp<-c() #make a vector for SNP
for (i in 1:ncol(data)) {
  if (length(unique(data[,i])) > 1) {
    snp<-c(snp,i) #print the snp column number into the vector,
  } 
}

data<-data[,snp] #reduce the dataset to snp 
dim(data)

#2.calculate, print and visualise allele frequencies for each SNP
