install.packages('maps')
install.packages('mapdata')

require(maps)
require(mapdata)
require(ggplot2)

load("../data/GPDDFiltered.RData")
head(gpdd)

world<-map_data("world")
head(world)
tail(world)
dim(world)
map<-ggplot() + geom_polygon(data = world, aes(x=long, y = lat, group = group)) 
map<-map + geom_point(data=gpdd, aes(x=long, y=lat), colour = "lightgreen")
map


#Looking at the map, what biases might you expect in any analysis based on the data represented? 
#The data is not equally spread geographically, therefore will be biased in terms of getting the global dynamics of species
#and not truly sampled in a global scale (small sample size and biased sampling in certain locations)
#not true global scale.

