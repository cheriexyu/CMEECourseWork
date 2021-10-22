#Using next in control flow to next iteration of a loop
#code checks if a number is odd using a modulo operation and prints it out 
for (i in 1:10){
  if ((i %% 2) == 0) #check if number is odd, %% modular division, if remainder is 0
    next #pass to next iteration of loop
  print(i)
}
