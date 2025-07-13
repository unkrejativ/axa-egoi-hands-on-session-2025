#%%
import subprocess
import pandas as pd

#%%
subprocess.run(['python', 'adapt_freq.py'], check=True)

#%%
url_sev_old="../original/freMTPL2sev.csv"
url_sev_new="insurance_claims_sev.csv"
url_freq="insurance_claims_freq.csv"

#%%
insurance_claims_sev=pd.read_csv(url_sev_old)
insurance_claims_freq=pd.read_csv(url_freq)

#%%

# ID is in freq and greater equal to 18
valid_ids = insurance_claims_freq.loc[insurance_claims_freq["DrivAge"] >= 18, "IDpol"]

# filter severity data and write to csv
sev_cleaned_pol = insurance_claims_sev[insurance_claims_sev["IDpol"].isin(valid_ids)]
sev_cleaned_pol.to_csv(url_sev_new, index=False)

# %%
insurance_claims_freq = insurance_claims_freq.drop(columns=["DrivAge"])
freq_cleaned_pol = insurance_claims_freq[(insurance_claims_freq['IDpol'].isin(sev_cleaned_pol['IDpol'])) | (insurance_claims_freq['ClaimNb']==0)]
freq_cleaned_pol.to_csv(url_freq, index=False)
