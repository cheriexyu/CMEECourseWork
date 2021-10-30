require(tidyverse)
require(ggplot2)
library(plyr)
MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")
head(MyDF)
str(MyDF)

a <- ggplot(MyDF,aes(x=Prey.mass, y=Predator.mass, colour=Predator.lifestage)) 
a <- a + geom_point(shape = I(3)) + facet_grid( Type.of.feeding.interaction~.) + scale_y_continuous(trans = 'log10') + theme_bw() + theme(panel.grid.minor = element_blank()) + geom_smooth(method = "lm",size=0.5,fullrange=TRUE) + scale_x_continuous(trans = 'log10') 
a <- a + xlab("Prey Mass in grams") + ylab("Predator mass in grams") + theme(legend.position="bottom", legend.title=element_text(face="bold"), legend.box="horizontal") 
a <- a + guides(colour = guide_legend(nrow = 1)) + theme(plot.margin = unit(c(1,3,1,3), "cm"))
a

#### Save figures a pdf in result folder
pdf("../results/PP_Regress.pdf",height=10,width=7)
print(a)
graphics.off()

#### Calculate regression results acording the lines in figure and save as csv
MyDF$Type.of.feeding.interaction<-as.factor(MyDF$Type.of.feeding.interaction)
str(MyDF)
MyDF$Predator.lifestage<-as.factor(MyDF$Predator.lifestage)
str(MyDF)

#Insectivorous
fig1<-lm(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="insectivorous"])~log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="insectivorous"]))
summary(fig1)

#piscivorous
install.packages("lme4")
library(lme4)
count(piscivorous$lifestage) # 5 lines
fig2<-lmer(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="piscivorous"])~log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="piscivorous"])*MyDF$Predator.lifestage[MyDF$Type.of.feeding.interaction=="piscivorous"])
summary(fig2)

#planktivorous
count(MyDF$Predator.lifestage[MyDF$Type.of.feeding.interaction=="planktivorous"]) # 5 lines
fig3<-lm(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="planktivorous"])~log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="planktivorous"])*MyDF$Predator.lifestage[MyDF$Type.of.feeding.interaction=="planktivorous"])
summary(fig3)

#predacious
count(MyDF$Predator.lifestage[MyDF$Type.of.feeding.interaction=="predacious"]) # 6 lines
fig4<-lm(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="predacious"])~log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="predacious"])*MyDF$Predator.lifestage[MyDF$Type.of.feeding.interaction=="predacious"])
summary(fig4)

#Predacious/piscivorous
count(MyDF$Predator.lifestage[MyDF$Type.of.feeding.interaction=="predacious/piscivorous"]) # 1 line
fig5<-lm(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="predacious/piscivorous"])~log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="predacious/piscivorous"]))
summary(fig5)

#DataFrame

#Done with v1,v2,v3

v1<-c("FeedingType x PredatorLifeStage","Insectivorous x larva/juvenile","Piscivorous x adult","Piscivorous x juvenile","Piscivorous x larva/juvenile","Piscivorous x postlarva","Piscivorous x postlarva/juvenile",
      "Planktivorous x adult","Planktivorous x juvenile","Planktivorous x larva","Planktivorous x larva/juvenile", "Planktivorous x postlarva/juvenile",
      "Predacious x adult","Predacious x juvenile","Predacious x larva","Predacious x larva/juvenile","Predacious x postlarva","Predacious x postlarva/juvenile","Predacious/piscivorous x adult")
v2<-c("Regression Slope","0.3842","0.285409","0.22348","0.652631","0.106773","NA","0.80276","0.16891","0.20422","0.53754","0.67548","0.321994","0.932339","0.323614","0.512543","0.154038","0.211648","0.54103")
v3<-c("Regression Intercept","-0.4109","3.042309","3.7887597","2.157279","-1.097665","0.68524","3.87815","1.13499","-0.87915","2.20757","2.95889","3.356362","3.098729","0.621931","1.564958","-0.694844","0.724032","2.07757")
v4<-c("R squared","0.1256","")
v5<-c("F statistic value","4.308")
v6<-c("Overall regression p-value","p=0.0466")

test<-data.frame(col1=v1,col2=v2,col3=v3)



Output<-as.data.frame()
Output<-read.csv("../results/PP_Regress_Results.csv", header = TRUE)
write.table(MyData[1,], file = "../results/MyData.csv",append=TRUE)
