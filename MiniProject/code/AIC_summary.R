library(dplyr)

#reads files
samplesize<-read.csv("../data/sample_size.csv")
AICc<-read.csv("../data/AICc_output.csv")
scale_AIC<-read.csv("../data/scaled_aicc.csv")
AIC_weight<-read.csv("../data/akaike_weight.csv")
AIC<-read.csv("../data/AIC_output.csv") 

samplesize = samplesize[-1,] #delete first row and second row due to the lack of parameters
samplesize = samplesize[-1,] #delete first row and second row due to the lack of parameters
head(samplesize)

samplesize %>% arrange(ID) #arrange in ascending order
table <- samplesize %>% slice(rep(1:n(), each = 3)) #repeat the sample size by an index of 3
table <- table %>% arrange(ID)


AIC <- as.data.frame(AIC,stringsAsFactors = F)
AIC_new <- pivot_longer(AIC, cols=3:5, names_to = "Model",values_to = "AIC", values_drop_na = FALSE) #pivot to long data frame

right_join(AIC_new,table,by="ID")
final<- bind_cols(AIC_new,table$Sample_Size)
names(final)[5] <- "Sample Size (N)"
final = subset(final, select = -c(X))
final<- final %>% relocate(`Sample Size (N)`, .after=Model)
head(final)

AICc <- pivot_longer(AICc, cols=2:4, names_to = "Model",values_to = "AICc", values_drop_na = FALSE)
final<- bind_cols(final,AICc$AICc)
names(final)[5] <- "AICc"

scale_AIC <- pivot_longer(scale_AIC, cols=2:4, names_to = "Model",values_to = "∆AIC", values_drop_na = FALSE)
final<- bind_cols(final,scale_AIC$"∆AIC")
names(final)[6] <- "ΔAICci"

head(AIC_weight)
AIC_weight<- pivot_longer(AIC_weight, cols=2:4, names_to = "Model",values_to = "Wi", values_drop_na = FALSE)
final<- bind_cols(final,AIC_weight$Wi)
names(final)[7] <- "Wi"

final$AIC <- round(final$AIC, digits=2) #final dataframe with concatenated AIC dataframes
final$AICc <- round(final$AICc, digits=2)
final$ΔAICci <- round(final$ΔAICci, digits=2)
final$Wi <- round(final$Wi, digits=2)


write.csv(final, "../data/AIC_final.csv", row.names=FALSE)

new <- final
new <- filter(final, ΔAICci == 0) #filter best fitted model for each ID
write.csv(new, "../data/filtered_AIC_final.csv", row.names=FALSE)



