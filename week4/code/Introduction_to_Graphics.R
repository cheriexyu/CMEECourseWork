##Dependencies##
install.packages("lattice")
library(ggplot2)
data("iris")

## Histograms
hist1<- ggplot(iris, aes(x=Petal.Length))+
  geom_histogram()
print(hist1)

hist2<- ggplot(iris, aes(x=Petal.Length))+
  geom_histogram(bins=20)
print(hist2)

hist3<- ggplot(iris, aes(x=Petal.Length, fill=Species))+
  geom_histogram(bins=20)
print(hist3)

#Barchart#
means <- iris%>%group_by(Species)%>%summarise(Petal.Width = mean(Petal.Width))
bar1<-ggplot(means, aes(y=Petal.Width, x=Species))+
  geom_bar(stat = "identity")
print(bar1)

#Dotcharts#
dot1<- ggplot(iris, aes(y=Petal.Width, x=Species))+
  geom_dotplot(binaxis = "y", stackdir = "center", binwidth = 1/30)+ 
  geom_point(means, mapping=aes(y=Petal.Width, x=Species), col="red", size=3)
print(dot1)

#Boxplot#
box1<- ggplot(iris, aes(y=Petal.Width, x=Species))+
  geom_boxplot()
print(box1)

#Scatterplots#
scatter1<- ggplot(iris, aes(y=Petal.Width, x=Sepal.Width))+
  geom_point()
print(scatter1)

#Scatter with Groups#
scatter2<- ggplot(iris, aes(y=Petal.Width, x=Sepal.Width, color=Species))+
  geom_point()
print(scatter2)

#Scatter with Facets#
scatter3<- ggplot(iris, aes(y=Petal.Width, x=Sepal.Width))+
  geom_point()+
  facet_grid(.~Species) #horizontal 
print(scatter3)

scatter4<- ggplot(iris, aes(y=Petal.Width, x=Sepal.Width))+
  geom_point()+
  facet_grid(Species~.) #vertical 
print(scatter4)

#Adding Titles#
scatter5<- ggplot(iris, aes(y=Petal.Width, x=Sepal.Width))+
  geom_point()+
  labs(x="Sepal Width (mm)", y="Petal Width (mm)", title="Petal vs Sepal")
print(scatter5)

#Changing Point Characters#
scatter6<- ggplot(iris, aes(y=Petal.Width, x=Sepal.Width))+
  geom_point(size=2, shape=11)+
  labs(x="Sepal Width (mm)", y="Petal Width (mm)", title="Petal vs Sepal")
print(scatter6)
