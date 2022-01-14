##if Statements##
sparrows <- 12
crows <- 5
if(sparrows>crows){
  print("Sparrows dominate")
}

#Example with Logical Variale#
a <- TRUE
if(a==TRUE){
  print("a is TRUE")
}

#Examples Numeric#
x <- 5
if(x > 0){
  print("Positive number")
}

##else Statements##
sparrows<- 5
crows<-12
if(sparrows>crows){
  print("Sparrows dominate")
} else{
  print("Crows dominate")
}

#Example#
a <- FALSE
if (a != TRUE){
  print ("a is FALSE")
} else {
  print ("a is TRUE")
}

#Example#
x <- 5
if(x > 0){
  print("Non-negative number")
} else {
  print("Negative number")
}

#Example#
b <- c(1, 2, 3, 4, -5, -7)
if(b>0){
  print("non-negative number")
} else {
  print("negative number")
}

##ifelse rewrites##
b <- c(1, 2, 3, 4, -5, -7)
ifelse(b>0,print(paste("non-negative number")),print(paste("negative number")))

#Simple#
a<- FALSE
ifelse(a=="FALSE", print("Is false"), print("Is true"))

x <- -5
ifelse(x>0, print("Non-negative number"), print("Negative number"))

a <- c("TRUE", "FALSE", "TRUE")
ifelse(a=="FALSE", print("Is false"), print("Is true"))

#A Quick Test#
b <- seq(from =1, to=10, by=2)
result <-ifelse(b!=3, print("No"), print("Yes"))
result[2]
b[2]

##for Loops##
for(i in 1:10){
  print(i)
}

#More#
for (i in 1:10){
  j <- i * i
  print(paste(i, " squared is", j ))
}


# For loop over vector of strings#
for(species in c('Heliodoxa rubinoides',
                 'Boissonneaua jardini',
                 'Sula nebouxii')){
  print(paste('The species is', species))
}

# for loop using a vector#
v1 <- c("a","bc","def")
for (i in v1){
  print(i) 
  }

##For, if and else##
z <- rnorm(10) #rnorm here is a random number generator#
for(i in z){
  if(i>0){
    print("TRUE")}
    else{
      print("FALSE")
    }
}

output<-ifelse(z>0, print("TRUE"), print("FALSE"))
