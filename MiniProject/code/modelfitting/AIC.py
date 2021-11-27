#!/usr/bin/env python3
#############################
# AIC rescaling 
#############################
aic = pd.read_csv("../../data/AIC_output.csv")

aic_drop=aic.dropna(axis=0,how ='all',subset=["Quadratic","Cubic","Gompertz"]) #drop rows with ALL NA
cubic_aic = aic_drop["Cubic"].to_numpy(na_value=np.nan)
quadratic_aic = aic_drop["Quadratic"].to_numpy(na_value=np.nan)
gompertz_aic = aic_drop["Gompertz"].to_numpy(na_value=np.nan)
ID_aic = aic_drop["ID"].to_numpy(dtype=object)

sample_size = pd.read_csv("../../data/sample_size.csv")
sample_size.sort_values(by=['ID'],inplace=True)
size = sample_size["Sample_Size"].to_numpy() #Array of samples sizes 


aicc = np.ones((273,3)) #273 after dropping all NAs, preallocate vector

aicc_cubic = [cubic_aic[m] * ( size[m] / (size[m] - 4 - 1)) for  m in range(len(cubic_aic))]
aicc_quadratic = [quadratic_aic[m] * ( size[m] / (size[m] - 3 - 1)) for  m in range(len(cubic_aic))]
aicc_gompertz = [gompertz_aic[m] * ( size[m] / (size[m] - 4 - 1)) for  m in range(len(cubic_aic))]

aicc[:,0] = aicc_cubic
aicc[:,1] = aicc_quadratic
aicc[:,2] = aicc_gompertz


aicc_df = pd.DataFrame(aicc,columns=["Cubic","Quadratic","Gompertz"])
aicc_df["ID"] = ID_aic
aicc_df.set_index('ID', inplace=True)

aicc_df.to_csv("../../data/AICc_output.csv",sep=',',na_rep="NA")