# CMEE 2021 HPC excercises R code HPC run code proforma

rm(list=ls()) # good practice in this instance
source("cy221/cy221_HPC_2021_main.R")
# it should take a faction of a second to source your file
# if it takes longer you're using the main file to do actual simulations
# it should be used only for defining functions that will be useful for your cluster run and which will be marked automatically

# do what you like here to test your functions (this won't be marked)
# for example
#print(species_richness(c(1,4,4,5,1,6,1)))
# should return 4 when you've written the function correctly for question 1

# you may also like to use this file for playing around and debugging
# but please make sure it's all tidied up by the time it's made its way into the main.R file or other files.
#init_community_max(7)
#init_community_min(4)

#species_richness(init_community_min(10)) #good no matter what it is one 
#species_richness(init_community_max(6)) #good 

#choose_two(4)

#neutral_step(c(10,5,13))
#neutral_generation(c(10,5,15))

#neutral_time_series(community = init_community_max(7) , duration = 20)
#neutral_time_series_speciation(community = init_community_max(7),speciation_rate = 0.1, duration = 20)
#neutral_step_speciation(c(10,5,13),0.2)

#species_abundance(c(1,5,3,6,5,6,1,1))

#octaves(c(100,64,63,5,4,3,2,2,1,1,1,1))

#question_16()

#Using Proc Time and isolating elapsed time 
#ptm<-proc.time() # start timer
#for(i in 1:1000){
  #print("happy")
#}
#test <- proc.time() - ptm # stop timer

#x = c()
#for (y in 1:5){
  #y<- 5
  #x <- c(x,y)
#}


#b <- c()
 #for (i in 1:5){
    #y <- list(octaves(c(100,62,2,5,61,1,1,1)))
    #b<- c(b,y)
    #}

#test<-list_oct
#write.csv(test,".csv")

#richness_vec <-c(richness_vec,richness)

cluster_run(speciation_rate = 0.1, size=100, wall_time=3, interval_rich=1, interval_oct=10, burn_in_generations=200, output_file_name='happy.rda') 


iter = 2
cluster_run(speciation_rate = 0.1, size=100, wall_time=3, interval_rich=1, interval_oct=10, burn_in_generations=200, output_file_name=paste('my_test_file',iter,'.rda', sep='_'))


for (iter in 1:30){
  if(iter < 9){
    print("cat")}
  if( 10 <= iter < 20 ){
    print("dog")
  }else{
    print("monkey")
  }
}




