require(tidyverse)
require(ggplot2)
require(tidyr)
library(dplyr)
library(broom)

MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")
MyDF$Type.of.feeding.interaction<-as.factor(MyDF$Type.of.feeding.interaction)
MyDF$Predator.lifestage<-as.factor(MyDF$Predator.lifestage)

a <- ggplot(MyDF,aes(x=Prey.mass, y=Predator.mass, colour=Predator.lifestage)) 
a <- a + geom_point(shape = I(3)) + facet_grid( Type.of.feeding.interaction~.) + scale_y_continuous(trans = 'log10') + theme_bw() + theme(panel.grid.minor = element_blank()) + geom_smooth(method = "lm",size=0.5,fullrange=TRUE) + scale_x_continuous(trans = 'log10') 
a <- a + xlab("Prey Mass in grams") + ylab("Predator mass in grams") + theme(legend.position="bottom", legend.title=element_text(face="bold"), legend.box="horizontal") 
a <- a + guides(colour = guide_legend(nrow = 1)) + theme(plot.margin = unit(c(1,3,1,3), "cm"))
a

#### Save figures a pdf in result folder
pdf("../results/PP_Regress.pdf",height=10,width=8)
print(a)
graphics.off()

#### Calculate regression results acording the lines in figure and save as csv

#Insectivorous
fig1<-lm(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="insectivorous"])~log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="insectivorous"]))
Insect_summary1<-tidy(summary(fig1))
Insect_summary2<-glance(fig1)

Insect_summary1<-Insect_summary1 %>% pivot_wider(names_from="term",values_from = c(estimate,std.error,statistic,p.value)) #convert to wide format

name<-c("larva / juvenile")
Insect_data<-data.frame(name,Insect_summary1[1:2],Insect_summary2[1],Insect_summary2[4:5])
colnames(Insect_data)[2] <- "Intercept"
colnames(Insect_data)[3] <- "Slope"


#piscivorous # 5 lines
table<-data.frame(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="piscivorous"]),log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="piscivorous"]), MyDF$Predator.lifestage[MyDF$Type.of.feeding.interaction=="piscivorous"])
names(table)[1] <- "Predatormass"
names(table)[2] <- "Preymass"
names(table)[3] <- "Lifestage"
str(table)


pis_summary1<-table %>% group_by(Lifestage) %>%
  do(fitHour = tidy(lm(Predatormass~Preymass, data=.))) %>% 
  unnest(fitHour)

pis_summary1<-pis_summary1 %>% pivot_wider(names_from="term",values_from = c(estimate,std.error,statistic,p.value)) #convert to wide format

pis_summary2<-table %>% group_by(Lifestage) %>%
  do(fitHour = glance(lm(Predatormass~Preymass, data=.))) %>% 
  unnest(fitHour)

pis_data<-data.frame(pis_summary1[1:3],pis_summary2[2],pis_summary2[5:6])
colnames(pis_data)[1] <- "name"
colnames(pis_data)[2] <- "Intercept"
colnames(pis_data)[3] <- "Slope"

#planktivorous
table2<-data.frame(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="planktivorous"]),log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="planktivorous"]), MyDF$Predator.lifestage[MyDF$Type.of.feeding.interaction=="planktivorous"])
names(table2)[1] <- "Predatormass"
names(table2)[2] <- "Preymass"
names(table2)[3] <- "Lifestage"
str(table2)

plank_summary1<-table2 %>% group_by(Lifestage) %>%
  do(fitHour = tidy(lm(Predatormass~Preymass, data=.))) %>% 
  unnest(fitHour)

plank_summary1<-plank_summary1 %>% pivot_wider(names_from="term",values_from = c(estimate,std.error,statistic,p.value)) #convert to wide format

plank_summary2<-table2%>% group_by(Lifestage) %>%
  do(fitHour = glance(lm(Predatormass~Preymass, data=.))) %>% 
  unnest(fitHour)

plank_data<-data.frame(plank_summary1[1:3],plank_summary2[2],pis_summary2[5:6])
colnames(plank_data)[1] <- "name"
colnames(plank_data)[2] <- "Intercept"
colnames(plank_data)[3] <- "Slope"

#predacious
table3<-data.frame(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="predacious"]),log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="predacious"]), MyDF$Predator.lifestage[MyDF$Type.of.feeding.interaction=="predacious"])
names(table3)[1] <- "Predatormass"
names(table3)[2] <- "Preymass"
names(table3)[3] <- "Lifestage"
str(table3)

pred_summary1<-table3 %>% group_by(Lifestage) %>%
  do(fitHour = tidy(lm(Predatormass~Preymass, data=.))) %>% 
  unnest(fitHour)

pred_summary1<-pred_summary1%>% pivot_wider(names_from="term",values_from = c(estimate,std.error,statistic,p.value)) #convert to wide format

pred_summary2<-table3 %>% group_by(Lifestage) %>%
  do(fitHour = glance(lm(Predatormass~Preymass, data=.))) %>% 
  unnest(fitHour)

pred_data<-data.frame(pred_summary1[1:3],pred_summary2[2],pred_summary2[5:6])
colnames(pred_data)[1] <- "name"
colnames(pred_data)[2] <- "Intercept"
colnames(pred_data)[3] <- "Slope"

#Predacious/piscivorous
fig5<-lm(log10(MyDF$Predator.mass[MyDF$Type.of.feeding.interaction=="predacious/piscivorous"])~log10(MyDF$Prey.mass[MyDF$Type.of.feeding.interaction=="predacious/piscivorous"]))
pred_pis_summary1<-tidy(summary(fig5))
pred_pis_summary2<-glance(fig5)

pred_pis_summary1<-pred_pis_summary1 %>% pivot_wider(names_from="term",values_from = c(estimate,std.error,statistic,p.value)) #convert to wide format
colnames(pred_pis_summary1)[1] <- "Intercept"
colnames(pred_pis_summary1)[2] <- "Slope"

name2<-c("adult")
pred_pis_data<-data.frame(name,pred_pis_summary1[1:2],pred_pis_summary2[1],pred_pis_summary2[4:5])
colnames(pred_pis_data)[1] <- "name"

#DataFrame

Feeding_Type<-c("Insectivorous","Piscivorous","Piscivorous","Piscivorous","Piscivorous","Piscivorous",
      "Planktivorous","Planktivorous","Planktivorous","Planktivorous", "Planktivorous",
      "Predacious","Predacious","Predacious","Predacious","Predacious","Predacious","Predacious/piscivorous")
v2<-data.frame(Feeding_Type)

a<-dplyr::bind_rows(Insect_data,pis_data,plank_data,pred_data,pred_pis_data)

final<-data.frame(Feeding_Type,a)
colnames(final)[2] <- "Predator.Lifestage"
colnames(final)[6] <- "F.statistic"

write.csv(final,"../results/PP_Regress_Results.csv")
