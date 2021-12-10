# CMEE 2021 HPC excercises R code main pro forma
# you don't HAVE to use this but it will be very helpful.  If you opt to write everything yourself from scratch please ensure you use EXACTLY the same function and parameter names and beware that you may loose marks if it doesn't work properly because of not using the proforma.

name <- "Cherie Yu"
preferred_name <- "Cherie"
email <- "cy221@imperial.ac.uk"
username <- "cy221"

# please remember *not* to clear the workspace here, or anywhere in this file. If you do, it'll wipe out your username information that you entered just above, and when you use this file as a 'toolbox' as intended it'll also wipe away everything you're doing outside of the toolbox.  For example, it would wipe away any automarking code that may be running and that would be annoying!

# Question 1
species_richness <- function(community){
  return(length(unique(community,incomparables=FALSE)))
}

# Question 2
init_community_max <- function(size){
  return(seq(from=1,to=size, by=1))
}

# Question 3
init_community_min <- function(size){
  return(rep(1,each=size))
}

# Question 4
choose_two <- function(max_value){
  return(sample(max_value,size=2,replace=FALSE))
}

# Question 5
neutral_step <- function(community){
  index = choose_two(length(community))
  community[index[2]]=community[index[1]]
  return (community)
}

# Question 6
neutral_generation <- function(community){
  generation <- 0
    if (length(community) %% 2 == 0){ #even number
      generation = length(community)/ 2
    } else{ #odd number, randomly choose to round up or down to whole number  
      out <- sample(1:2, size=1)
        if (out == 1){
          generation = floor(length(community)/2)
        } else {
          generation = ceiling(length(community)/2)
        }
      }
  
  for (i in 1:(generation)){
    community = neutral_step(community)
  }
  return (community)
}

# Question 7
neutral_time_series <- function(community,duration) {
  time = c(species_richness(community))
  for (i in 1:duration){
    community = neutral_generation(community)
    time = c(time,species_richness(community))
  }
  return (time)
}

# Question 8
question_8 <- function() {
  model<-neutral_time_series(community = init_community_max(100) , duration = 200)
  plot(model,pch=16,cex=0.5, col="blue",xlab="Time(Generation)",ylab="Species richness per generation")
  # clear any existing graphs and plot your graph within the R window
  return("It will eventually converge to a species richness of one. At one point all death will be replaced by the same species. All species cannot go extinct as the remaining one will always be replaced by the same species and the number of individual is fixed in my model.")
}

# Question 9
neutral_step_speciation <- function(community,speciation_rate){
  probability <- runif(1)
  if (probability<=speciation_rate){
    index = choose_two(length(community))
    community[index[2]]= max(community)+1
    return (community)
  }else{
    neutral_step(community)
    }
}
# Question 10
neutral_generation_speciation <- function(community,speciation_rate)  {
  generation <- 0
  if (length(community) %% 2 == 0){ #even number
    generation = length(community)/ 2
  } else{ #odd number, randomly choose to round up or down to whole number  
    out <- sample(1:2, size=1)
    if (out == 1){
      generation = floor(length(community)/2)
    } else {
      generation = ceiling(length(community)/2)
    }
  }
  
  for (i in 1:(generation)){
    community = neutral_step_speciation(community,speciation_rate)
  }
  return (community)
}

# Question 11
neutral_time_series_speciation <- function(community,speciation_rate,duration)  {
  time = c(species_richness(community))
  for (i in 1:duration){
    community = neutral_generation_speciation(community,speciation_rate)
    time = c(time,species_richness(community))
  }
  return (time)
}

# Question 12
question_12 <- function()  {
  # clear any existing graphs and plot your graph within the R window
  model_speciation<-neutral_time_series_speciation(community = init_community_max(100) , 0.1, duration = 200)
  initial<-neutral_time_series_speciation(community = init_community_min(100) , 0.1, duration = 200)
  plot(model_speciation,col="red",type="l",pch=16,cex=0.5,xlab="Time(Generation)",ylab="Species richness per generation",ylim=c(0,100),main="Neutral theory simulation with speciation rate=0.1, community size=100, generations=200",cex.main=0.7)
  lines(initial,col="blue",pch=16,cex=0.5)
  legend(100, 100, legend=c('Inital community with a maximum of 100 species', 'Inital community with only one species'), pch=c(16, 16), col=c('red', 'blue'), cex=0.6,bty = "n")
  return("The effect of initial condition does not seem to have showed different result as time increases, both communities fluctuates in a fixed state, within simillar species richness, which means it reaches equilibrium (speciation brings new specieis, death(extinction) kills off species.")
}

# Question 13
species_abundance <- function(community){
community <- table(community)
community <- sort(community, decreasing = TRUE)
abundance<-as.vector(community)
return(abundance)
}

# Question 14
octaves <- function(abundance_vector) {
    abundance_vector=floor(log2(abundance_vector)+1)
    abundance_vector<-tabulate(abundance_vector)
    return(abundance_vector)
}

# Question 15
sum_vect <- function(x, y) {
  if (length(x)>length(y)){
    diff=length(x)-length(y)
    y=c(y,rep(0,diff))
  }else{
    diff=length(y)-length(x)
    x=c(x,rep(0,diff))
  }
  
  total = x + y
  return(total)
}
# Question 16 
question_16 <- function(){
  # clear any existing graphs and plot your graph within the R window
  community_max = init_community_max(100) #1
  community_min = init_community_min(100) #2

  for (x in 1:200){
    community_max = neutral_generation_speciation(community_max,0.1)
    community_min = neutral_generation_speciation(community_min,0.1)
  }
  
  abundance_1<-species_abundance(community_max)
  abundance_2<-species_abundance(community_min)
  octaves(abundance_1)
  octaves(abundance_2)

  running_sum_1 = octaves(abundance_1)
  running_sum_2 = octaves(abundance_2)

  for(y in 1:2000){
    community_max = neutral_generation_speciation(community_max,0.1)
    community_min = neutral_generation_speciation(community_min,0.1)
      if (y %% 20 == 0){
        abundance_community_max<-species_abundance(community_max)
        abundance_community_min<-species_abundance(community_min)
        sum_1 <- octaves(abundance_community_max)
        sum_2 <- octaves(abundance_community_min)
        running_sum_1 = sum_vect(running_sum_1,sum_1) 
        running_sum_2 = sum_vect(running_sum_2,sum_2)
      }
  }

  community_max_sum <- running_sum_1 / 100
  community_min_sum <- running_sum_2 / 100
  
  plot<-data.frame(community_max_sum,community_min_sum)
  bin=c(1,"2-3","4-7","8-15","16-31","32-63")
  editplot<-t(plot)
  colnames(editplot) <- bin
  barplot(height=editplot,beside=TRUE, ylim=c(0,12), xlab="Number of individuals per species", ylab="Number of Species", main="Mean species abundance distribution represented by octaves for two initial communities (size=100), over 2,200 generations",cex.main=0.7, col=c("pink","lightgreen"))
  legend("topright", legend=c("Inital community with a maximum of 100 species","Inital community with only one species"),fill=c("lightpink","lightgreen"),cex=0.7,bty = "n")
return("The initial condition of the system does not matter as both communities achieved simillar number of individuals per species. This is because in inital communities with maximum species, extinction rate is high. In initial communities with only one species, extinction rate is low. Eventually over generations, extinction rates will reach an equalibrium with speciation rate and both communities will converge to simillar number of indivduals per species.")
}
# Question 17
cluster_run <- function(speciation_rate, size, wall_time, interval_rich, interval_oct, burn_in_generations, output_file_name){
  richness_vec = c()
  list_oct = c()
  initial_community = init_community_min(size)
  y = 1
  timer<-proc.time()[[3]]
  while (proc.time()[[3]] - timer < wall_time*60){
    initial_community <- neutral_generation_speciation(initial_community,speciation_rate)
    if (y %% interval_oct == 0){
      spp_abundance <- species_abundance(initial_community)
      oct <- list(octaves(spp_abundance))
      list_oct <- c(list_oct,oct)
    }
    if (y <= burn_in_generations){
      if (y %% interval_rich == 0){
        richness <- species_richness(initial_community)
        richness_vec <-c(richness_vec,richness)
      } #stops if outside burn in generations, goes to next loop
    }
    y = y+1
    end_time <- proc.time()[[3]]
    total_time <- end_time - timer
  }
  save(richness_vec,list_oct,initial_community,speciation_rate,size,wall_time,interval_rich,interval_oct,burn_in_generations,total_time,file = output_file_name)
}

# Questions 18 and 19 involve writing code elsewhere to run your simulations on the cluster

# Question 20 
process_cluster_results <- function()  {
  combined_results <- list() #create your list output here to return
  # save results to an .rda file
  
}

plot_cluster_results <- function()  {
    # clear any existing graphs and plot your graph within the R window
    # load combined_results from your rda file
    # plot the graphs
    
    return(combined_results)
}

# Question 21
question_21 <- function()  {
    
  return("type your written answer here")
}

# Question 22
question_22 <- function()  {
    
  return("type your written answer here")
}

# Question 23
chaos_game <- function()  {
  # clear any existing graphs and plot your graph within the R window
  
  return("type your written answer here")
}

# Question 24
turtle <- function(start_position, direction, length)  {
    
  return() # you should return your endpoint here.
}

# Question 25
elbow <- function(start_position, direction, length)  {
  
}

# Question 26
spiral <- function(start_position, direction, length)  {
  
  return("type your written answer here")
}

# Question 27
draw_spiral <- function()  {
  # clear any existing graphs and plot your graph within the R window
  
}

# Question 28
tree <- function(start_position, direction, length)  {
  
}

draw_tree <- function()  {
  # clear any existing graphs and plot your graph within the R window

}

# Question 29
fern <- function(start_position, direction, length)  {
  
}

draw_fern <- function()  {
  # clear any existing graphs and plot your graph within the R window

}

# Question 30
fern2 <- function(start_position, direction, length, dir)  {
  
}
draw_fern2 <- function()  {
  # clear any existing graphs and plot your graph within the R window

}

# Challenge questions - these are optional, substantially harder, and a maximum of 16% is available for doing them.  

# Challenge question A
Challenge_A <- function() {
  # clear any existing graphs and plot your graph within the R window

}

# Challenge question B
Challenge_B <- function() {
  # clear any existing graphs and plot your graph within the R window

}

# Challenge question C
Challenge_C <- function() {
  # clear any existing graphs and plot your graph within the R window

}

# Challenge question D
Challenge_D <- function() {
  # clear any existing graphs and plot your graph within the R window
  
  return("type your written answer here")
}

# Challenge question E
Challenge_E <- function() {
  # clear any existing graphs and plot your graph within the R window
  
  return("type your written answer here")
}

# Challenge question F
Challenge_F <- function() {
  # clear any existing graphs and plot your graph within the R window
  
  return("type your written answer here")
}

# Challenge question G should be written in a separate file that has no dependencies on any functions here.


