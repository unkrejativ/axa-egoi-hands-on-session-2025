#%%
import pandas as pd

url_old="../original/freMTPL2sev.csv"
url_new="insurance_claims_sev.csv"

#%%
insurance_claims_sev=pd.read_csv(url_old)
insurance_claims_sev.head()

#%%
# Write insurance_claims_sev
insurance_claims_sev.to_csv(url_new, index=False)