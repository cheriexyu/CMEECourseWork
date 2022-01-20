require("tidyverse")

MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")
dim(MyDF)
head(MyDF)
MyDF$Type.of.feeding.interaction <- as.factor(MyDF$Type.of.feeding.interaction)
MyDF$Location <- as.factor(MyDF$Location)
str(MyDF)
MyDF$Prey.mass <- ifelse(grepl("mg", MyDF$Prey.mass.unit), MyDF$Prey.mass*0.001, MyDF$Prey.mass) #Change mg to grams


########### Calculations ########
Ratio<-data.frame((MyDF$Prey.mass / MyDF$Predator.mass), MyDF$Type.of.feeding.interaction)
colnames(Ratio)
names(Ratio)[names(Ratio) == "X.MyDF.Prey.mass.MyDF.Predator.mass."] <- "Size.Ratio"
names(Ratio)[names(Ratio) == "MyDF.Type.of.feeding.interaction"] <-"Type.of.feeding.interaction"
head(Ratio)

Predator.mean.log10<-tapply(log10(MyDF$Predator.mass),MyDF$Type.of.feeding.interaction,mean)
Prey.mean.log10<-tapply(log10(MyDF$Prey.mass),MyDF$Type.of.feeding.interaction,mean)
Predator.Prey.Size.Ratios.mean.log10<-tapply(log10(Ratio$Size.Ratio),Ratio$Type.of.feeding.interaction,mean)
Predator.median.log10<-tapply(log10(MyDF$Predator.mass),MyDF$Type.of.feeding.interaction,median)
Prey.median.log10<-tapply(log10(MyDF$Prey.mass),MyDF$Type.of.feeding.interaction,median)
Predator.Prey.Size.Ratios.median.log10<-tapply(log10(Ratio$Size.Ratio),Ratio$Type.of.feeding.interaction,median)

calc<-data.frame(Predator.mean.log10,Prey.mean.log10,Predator.Prey.Size.Ratios.mean.log10, Predator.median.log10,Prey.median.log10,Predator.Prey.Size.Ratios.median.log10)
calc
calc<-tibble::rownames_to_column(calc,var="Feeding.Types") %>% head
write.csv(calc,"../results/PP_Results.csv")

######### 3 Figures #########
#Subplots of Distribution of Predator Mass by Feeding Interation type 
pdf("../results/Pred_Subplots.pdf",11.7, 8.3)  # Open blank pdf page using a relative path # These numbers are page dimensions in inches
par(mfrow=c(3,2)) #initialize multi-paneled plot # specify which sub-plot to use first 
hist(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="insectivorous"]), xlab = "log10 (Predator Mass (g))", ylab = "Insectivorous", main ="")
hist(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="piscivorous"]), xlab = "log10 (Predator Mass (g))", ylab = "Piscivorous" , main ="")
hist(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="planktivorous"]), xlab = "log10 (Predator Mass (g))", ylab = "Planktivorous" , main ="")
hist(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="predacious"]), xlab = "log10 (Predator Mass (g))", ylab = "Predacious" , main ="")
hist(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="predacious/piscivorous"]), xlab = "log10 (Predator Mass (g))", ylab = "Predacious/Piscivorous" , main ="")
mtext("Types of feeding interaction and Predator mass (g)",side = 3,line = - 2,outer = TRUE)
graphics.off(); #you can also use dev.off() 

#Subplots of Distribution of Prey Mass by Feeding Interation type 
pdf("../results/Prey_Subplots.pdf",11.7, 8.3) # Open blank pdf page using a relative path  # These numbers are page dimensions in inches
par(mfrow=c(3,2)) #initialize multi-paneled plot # specify which sub-plot to use first 
hist(log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="insectivorous"]), xlab = "log10 (Prey Mass (g))", ylab = "Insectivorous", main ="")
hist(log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="piscivorous"]), xlab = "log10 (Prey Mass (g))", ylab = "Piscivorous" , main ="")
hist(log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="planktivorous"]), xlab = "log10 (Prey Mass (g))", ylab = "Planktivorous" , main ="")
hist(log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="predacious"]), xlab = "log10 (Prey Mass (g))", ylab = "Predacious" , main ="")
hist(log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="predacious/piscivorous"]), xlab = "log10 (Prey Mass (g))", ylab = "Predacious/Piscivorous" , main ="")
mtext("Types of feeding interaction and Prey mass (g)",side = 3,line = - 2,outer = TRUE)
graphics.off(); #you can also use dev.off() 

#Subplots of size ratio of prey mass over predator mass by feeding interaction type
pdf("../results/SizeRatio_Subplots.pdf", 11.7, 8.3)# Open blank pdf page using a relative path
par(mfrow=c(3,2)) 
hist(log10(Ratio$Size.Ratio[Ratio$Type.of.feeding.interaction=="insectivorous"]), xlab = "log10 (Size ratio of prey mass over predator mass (g))", ylab = "insectivorous", main ="")
hist(log10(Ratio$Size.Ratio[Ratio$Type.of.feeding.interaction=="piscivorous"]), xlab = "log10 (Size ratio of prey mass over predator mass (g))", ylab = "piscivorous", main ="")
hist(log10(Ratio$Size.Ratio[Ratio$Type.of.feeding.interaction=="planktivorous"]), xlab = "log10 (Size ratio of prey mass over predator mass (g))", ylab = "planktivorous", main ="")
hist(log10(Ratio$Size.Ratio[Ratio$Type.of.feeding.interaction=="predacious"]), xlab = "log10 (Size ratio of prey mass over predator mass (g))", ylab = "predacious", main ="")
hist(log10(Ratio$Size.Ratio[Ratio$Type.of.feeding.interaction=="predacious/piscivorous"]), xlab = "log10 (Size ratio of prey mass over predator mass (g))", ylab = "predacious/piscivorous", main ="")
mtext("Types of feeding interaction and Size ratios of prey mass over predator mass (g)",side = 3,line = - 2,outer = TRUE)
graphics.off();