# CMEE 2021 HPC excercises R code HPC run code pro forma

rm(list=ls()) # good practice 
graphics.off()
source("cy221_HPC_2021_main.R")

iter <- as.numeric(Sys.getenv("PBS_ARRAY_INDEX")) #For HPC, the equvilent for this is the iter for loop 
set.seed(iter)
if(iter <= 25){
  size = 500}
if( iter > 25 && iter <= 50 ){
  size = 1000}
if( iter > 50 && iter <= 75){
  size = 2500}
if( iter > 75 && iter <= 100){
  size = 5000}
cluster_run(speciation_rate = 0.0025199, size=size, wall_time=11.5*60, interval_rich=1, interval_oct=size/10, 
            burn_in_generations=8*size, output_file_name=paste('cy221_cluster_run',iter,'.rda', sep='_'))


