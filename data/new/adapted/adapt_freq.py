#%%
import pandas as pd
import numpy as np
import random
from datetime import date, timedelta

url_old="../original/freMTPL2freq.csv"
url_new="insurance_claims_freq.csv"

#%%
insurance_claims_freq=pd.read_csv(url_old)
insurance_claims_freq.head()

#%%
#a=insurance_claims_freq[insurance_claims_freq["Exposure"] > 1.1]
#a[a["ClaimNb"] > 0]["IDpol"].unique() 22
#%%

# taken from Heiko's solution
insurance_claims_freq = insurance_claims_freq[insurance_claims_freq["Exposure"] <= 1.1]
insurance_claims_freq["Exposure"] = np.minimum( insurance_claims_freq["Exposure"], 1 )  

#%%
def random_birthdate_from_age(age):
    today = date(2025, 7, 16)
    
    max_date = today.replace(year=today.year - age)
    min_date = max_date.replace(year=max_date.year - 1) + timedelta(days=1)

    delta_days = (max_date - min_date).days
    random_days = random.randint(0, delta_days)
    
    return min_date + timedelta(days=random_days)


#%%
# Calculate Birth date
sub = [col for col in insurance_claims_freq.columns if col != 'IDpol']
unique_rows = insurance_claims_freq.drop_duplicates(subset=sub).copy()
unique_rows['DriverBirthDate'] = unique_rows["DrivAge"].apply(random_birthdate_from_age)


#%%

# repeat to calculate birth date for duplicates/collisions
compare_cols = [col for col in unique_rows.columns if col != "IDpol" and col != "Exposure"]

max_tries = 10
tries = 0

while unique_rows.duplicated(subset=compare_cols).any() and tries < max_tries:
    dupes = unique_rows[unique_rows.duplicated(subset=compare_cols, keep='first')].index
    unique_rows.loc[dupes, "DriverBirthDate"] = unique_rows.loc[dupes, "DrivAge"].apply(random_birthdate_from_age)
    tries += 1

if unique_rows.duplicated(subset=compare_cols).any():
    raise ValueError("Still duplicates left")


#%%
ssub = sub + ['DriverBirthDate']
insurance_claims_freq = insurance_claims_freq.merge(unique_rows[ssub], on=sub, how='left')

#%%
insurance_claims_freq = insurance_claims_freq.drop(columns=["Exposure", "DrivAge"])
insurance_claims_freq.head()

#%%
# for testing:
# should be 648919 rows left
# insurance_claims_freq.drop_duplicates(subset=[col for col in insurance_claims_freq.columns if col != 'IDpol' and col != 'Exposure'])
#%%
# Write insurance_claims_freq
insurance_claims_freq.to_csv(url_new, index=False)