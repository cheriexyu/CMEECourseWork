#If statements
a<-TRUE
if (a==TRUE){
  print("a is TRUE")
  }else{
  print ("a is FALSE")
  }
#Or can write an if statement on a single line as below
z <- runif(1)
if(z<=0.5) {print("less than a half")} #but avoid this because you cant read it 


#For Loops, useful to repeat a task over a range of input values
#Code loops over range, then squaring each and print results:
for(i in 1:20){
  j<-i*i #J temporary stores the variable in the loop
  print(paste(i,"squared is",j)) #paste() takes multiple elemnts and concatenate them into a single one
}
#Loop over a vector of strings:
for(species in c('Heliodoxa rubinoides','Boissonneaua jardini', 'Sula neboixii')){
  print(paste('The species is',species))
}
#Loop using a pre-existing vector:
v1<-c("a","bc","def")
for (i in v1){
  print(i)
}
#While Loops, perform an operation till some condition is met 
i <- 0
while(i<10){
  i<-i+1 #stores it in i, allow the value to increase in 1 till less than 10 then exit command
  print(i^2) 
}
#Breaking out of loops, break out of a loop when some condition is met
#Refer to break.R Script


