library(dplyr)
library(ggplot2)
library(minpack.lm)
t <- seq(0, 22, 2)
N <- c(32500, 33000, 38000, 105000, 445000, 1430000, 3020000, 4720000, 5670000, 5870000, 5930000, 5940000)

set.seed(1234) # To ensure we always get the same random sequence in this example "dataset" 

data <- data.frame(t, N * (1 + rnorm(length(t), sd = 0.1))) # add some random error

names(data) <- c("Time", "N")

head(data)

ggplot(data, aes(x = Time, y = N)) + geom_point(size = 3) +labs(x = "Time (Hours)", y = "Population size (cells)")

data$LogN <- log(data$N)

# visualise
ggplot(data, aes(x = t, y = LogN)) + 
  geom_point(size = 3) +
  labs(x = "Time (Hours)", y = "log(cell number)")

logistic_model <- function(t, r_max, K, N_0){ # The classic logistic equation
  return(N_0 * K * exp(r_max * t)/(K + N_0 * (exp(r_max * t) - 1)))
}

N_0_start <- min(data$N) # lowest population size
K_start <- max(data$N) # highest population size
r_max_start <- 0.62 # use our estimate from the OLS fitting from above

fit_logistic <- nlsLM(N ~ logistic_model(t = Time, r_max, K, N_0), data,
                      list(r_max=r_max_start, N_0 = N_0_start, K = K_start)) #minimized fit in R

timepoints <- seq(0, 22, 0.1)

logistic_points <- logistic_model(t = timepoints, 
                                  r_max = coef(fit_logistic)["r_max"], 
                                  K = coef(fit_logistic)["K"], 
                                  N_0 = coef(fit_logistic)["N_0"]) #starting parameters for nlsLM function

df1 <- data.frame(timepoints, logistic_points)

df1$model <- "Logistic equation"
names(df1) <- c("Time", "N", "model")

#Save plot in graphs directory as a pdf
pdf(file="graphs/example_data_logistic.pdf")
ggplot(data, aes(x = Time, y = N)) +geom_line(data = df1, aes(x = Time, y = N), size = 1) + theme(aspect.ratio=1)+ labs(x = "Time", y = "Log Growth")+ geom_text(x=18, y=5.7e+06, label="A") + 
  geom_text(x=10,y=3e+06,label= expression(paste(mu,"m"))) + geom_text(x=8, y=0, label=expression(paste(lambda)))
dev.off()







