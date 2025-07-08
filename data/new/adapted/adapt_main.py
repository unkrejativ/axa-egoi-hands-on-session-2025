#%%
import subprocess
import pandas as pd

#%%
subprocess.run(['python', 'adapt_freq.py'], check=True)

#%%
subprocess.run(['python', 'adapt_sev.py'], check=True)

#%%
# Join the data

url_freq="insurance_claims_freq.csv"
url_sev="insurance_claims_sev.csv"

freq=pd.read_csv(url_freq)
sev=pd.read_csv(url_sev)

only_in_freq = freq[~freq['IDpol'].isin(sev['IDpol'])]
# %%
only_in_freq
# %%
only_in_sev = sev[~sev['IDpol'].isin(freq['IDpol'])]
# %%
only_in_sev