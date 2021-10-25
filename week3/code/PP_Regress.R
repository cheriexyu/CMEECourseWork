MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")
head(MyDF)

a <- ggplot(MyDF,aes(x=Prey.mass, y=Predator.mass, colour=Predator.lifestage)) 
a <- a + geom_point(shape = I(3)) + facet_grid( Type.of.feeding.interaction~.) + scale_y_continuous(trans = 'log10') + theme_bw() + theme(panel.grid.minor = element_blank()) + geom_smooth(method = "lm",size=0.5,fullrange=TRUE) + scale_x_continuous(trans = 'log10') 
a <- a + xlab("Prey Mass in grams") + ylab("Predator mass in grams") + theme(legend.position="bottom", legend.title=element_text(face="bold"), legend.box="horizontal") 
a <- a + guides(colour = guide_legend(nrow = 1)) + theme(plot.margin = unit(c(1,3,1,3), "cm"))
a

#### Save figures a pdf in result folder
pdf("../results/PP_Regress.pdf")
print(a)
graphics.off()

#### Calculate regression results acording the lines in figure and save as csv
summary(lm(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="insectivorous"])~log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="insectivorous"])))

insect<-data.frame(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="insectivorous"],
                             MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="insectivorous"], MyDF$Predator.lifestage[MyDF$Type.of.feeding.interaction=="insectivorous"])
colnames(insect) <- c("Predator.mass", "Prey.mass","lifestage")
head(insect)
linear<-lm(log10(Predator.mass)~log10(Prey.mass),data=insect)
summary(linear)


piscivorous<-data.frame(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="piscivorous"],
                   MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="piscivorous"], MyDF$Predator.lifestage[MyDF$Type.of.feeding.interaction=="piscivorous"])
colnames(piscivorous) <- c("Predator.mass", "Prey.mass","lifestage")
head(piscivorous)
linear2<-lm(log10(Predator.mass)~log10(Prey.mass)+lifestage,data=piscivorous)
summary(linear2)

require(dplyr)
count(piscivorous,lifestage)
