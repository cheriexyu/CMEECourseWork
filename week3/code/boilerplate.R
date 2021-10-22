# A boilerplate R script 
MyFunction<-function(Arg1, Arg2){ #Curly brackets tells R where function start and ends
  
  #Statements involving Arg1,Arg2:
  print(paste("Argument", as.character(Arg1), "is a", class(Arg1))) #prints Arg1's type
  print(paste("Argument", as.character(Arg2), "is a", class(Arg2))) #prints Arg2's type
  
  return (c(Arg1, Arg2)) #this is optional, but very useful
}

#Functions
MyFunction(1,2) #test the function
MyFunction("Riki","Tiki") #A different test 

class(MyFunction) #Function onject
