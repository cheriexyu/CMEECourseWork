rm(list=ls()) 
graphics.off()
source("cy221/cy221_HPC_2021_main.R")

#iter <- as.numeric(Sys.getenv("PBS_ARRAY_INDEX")) #For HPC, the equvilent for this is the iter for loop 
for (iter in 1:100){
  set.seed(iter)
  if(iter < 25){
    size = 500}
  if( iter > 25 & iter < 50 ){
    size = 1000}
  if( iter > 25 & iter < 50){
    size = 2500
  }else{
    size = 5000
  }
  cluster_run(speciation_rate = 0.1, size=size, wall_time=2, interval_rich=1, interval_oct=size/10, 
              burn_in_generations=8*size, output_file_name=paste('my_test_file',iter,'.rda', sep='_'))
  #cluster_run(speciation_rate = 0.1, size=size, wall_time=12, interval_rich=1, interval_oct=size/10, 
              #burn_in_generations=8*size, output_file_name=paste('my_test_file',iter,'.rda', sep='_'))
}

for (iter in 1:10){
  set.seed(iter)
  if(iter < 2){
    size = 50}
  if( iter > 2 & iter < 5 ){
    size = 100}
  if( iter > 5 & iter < 8){
    size = 250
  }else{
    size = 500
  }
  cluster_run(speciation_rate = 0.1, size=size, wall_time=2, interval_rich=1, interval_oct=size/10, 
              burn_in_generations=8*size, output_file_name=paste('my_test_file',iter,'.rda', sep='_'))
}


