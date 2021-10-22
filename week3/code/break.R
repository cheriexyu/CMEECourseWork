#Breaking out of loops, stop the loop when some condition is met
i <- 0 #Initialize i
  while(i<Inf){ #while i is an positive infinity, storing numbers that can be divisible by 0
    if (i==10){
      break
        }
    else{
      cat("i equals", i, "\n")
      i<-i+1 #Updates i
    }
  }

