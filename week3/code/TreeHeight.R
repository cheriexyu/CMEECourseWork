#This function calculates heights of trees given distance of each tree
#from its base and angle to its top, using the trigonometric formula

#height = distance*tan(radians)

#ARGUMENTS
#degrees: the angle of elevation of tree
#distance: the distance from base of tree (e.g., meters)

#OUTPUT
#The heights of the tree, same units as "distance" 

TreeData<-read.csv("../data/trees.csv",header=TRUE)

TreeHeight <- function(degrees, distance){
  radians <- degrees * pi/180 #Equation 1
  height <- distance * tan(radians) #Main Equation
  print(paste("Tree height is:", height))
  
  return(height) 
}

#TreeHeight(37,40)
Height<-TreeHeight(TreeData$Angle.degrees,TreeData$Distance.m) 
output_tree <- data.frame(TreeData) #Make a new dataframe
output_tree["Tree.Height.m"] <- Height #Create a new column called height

write.csv(output_tree, "../results/TreeHts.csv") #write a new file 
