#A simple script to illustrate R input-output.
#Run line by line and check inputs outputs to understand what is happening 

MyData<-read.csv("../data/trees.csv", header=TRUE) #headers is true, import them as well
write.csv(MyData,"../results/MyData.csv")
write.table(MyData[1,],file="../results/MyData.csv",append=TRUE) #appending MyData file with new table
write.csv(MyData,"../results/MyData.csv", row.names=TRUE) #write row names from trees into MyData file
write.table(MyData,"../results/MyData.csv", col.names=FALSE) #write the table and ignore column names
print("Script complete!")
