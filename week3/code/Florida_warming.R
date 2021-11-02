#Are temperatures of one year significantly correlated with the next year 
#(successive years), across years in a given location? 

load("../data/KeyWestAnnualMeanTemperature.Rdata") #Temperature in KeyWest for the 20th Century
head(ats)
pdf("../code/keywest.pdf")
keywest<-plot(ats)
keywest<-abline(lm(ats$Temp~ats$Year),col="blue")
print(keywest)
graphics.off()

#Save it as a vector
Year<-ats[,1]
Year
is.vector(Year) #Check it is a vector
Temp<-ats[,2]
Temp
is.vector(Temp) #Check it is a vector

#approx correltation of year and temp
approx<-cor(Year,Temp,use="everything",method=c("pearson")) #correlation coefficent
approx
#0.5331784 is the approx correlation coefficent 

#Shuffle the temp then calculate a correlation coefficient, repeat by 10000
a <- rep(NA,10000) #pre=allocated vector for correlation coefficent
for (i in 1:10000){
  a[i] <- cor(Year,sample(Temp,replace=FALSE))
}
print(a)

#histagram of correlation coefficents
pdf("../code/histogram.pdf")
graph<-hist(a, xlab="Correlation Coefficent", ylab="Frequency", main="Histagram of Matrix", xlim=c(-0.5,0.7),ylim=c(0,2000))
abline(v = approx, col="blue", lwd=3, lty=2)
legend("top",legend="Observed correlation coefficient", col="blue",cex=0.4,lwd=3, lty=2)
print(graph)
graphics.off()

#Calculate what fraction of the random correlation coefficients were greater than the observed one (this is your approximate, asymptotic p-value).
length(a[a>approx]) #number of elements greater than approx in R 
#None are larger than 0 



