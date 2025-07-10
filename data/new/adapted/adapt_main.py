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
insurance_claims_sev.head()

#%%
insurance_claims_sev

#%%
sev_cleaned_pol = insurance_claims_sev[insurance_claims_sev['IDpol'].isin(insurance_claims_freq['IDpol'])]
sev_cleaned_pol
#%%
sev_cleaned_pol.to_csv(url_sev_new, index=False)
