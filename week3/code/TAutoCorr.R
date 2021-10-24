#Are temperatures of one year significantly correlated with the next year 
#(successive years), across years in a given location? 

load("../data/KeyWestAnnualMeanTemperature.Rdata") #Temperature in KeyWest for the 20th Century
head(ats)
plot(ats)
approx<-cor(Year,Temp) #correlation coefficent
approx
class(ats) #Dataframe

#Save it as a vector
keywest <- vect
is.vector(Year) #is it a vector
Year<-ats[,1]
Year
is.vector(Year) #Check it is a vector
Temp<-ats[,2]
Temp
is.vector(Temp) #Check it is a vector

#Shuffle the temp then calculate a correlation coefficent, repeat by 10000
a <- rep(NA,10000) #pre=allocated vector for correlation coefficent
for (i in 1:10000){
  a[i] <- cor(Year,sample(Temp,replace=TRUE))
}
print(a)

#histagram of correlation coefficents
hist(a, xlab="Correlation Coefficent", ylab="Frequency", main="Histagram of Matrix")

