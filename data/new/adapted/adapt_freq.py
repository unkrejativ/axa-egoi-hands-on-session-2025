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

# def generate_unique_birthdates(df, age_col, max_tries=10):
#     result = []
#     seen_rows = set()

#     for i, row in df.iterrows():
#         for _ in range(max_tries):
#             birthdate = random_birthdate_from_age(row[age_col])
#             reduced_row = row.drop(labels=["Exposure"])
            
#             # Neue Zeile mit BirthDate
#             reduced_row_with_date = tuple(reduced_row.tolist() + [birthdate])
#             if reduced_row_with_date not in seen_rows:
#                 seen_rows.add(reduced_row_with_date)
#                 result.append(birthdate)
#                 break
#         else:
#             raise ValueError(f"Could not find a unique date for {i} after {max_tries} retries.")
    
#     return result

#%%
sub = [col for col in insurance_claims_freq.columns if col != 'IDpol']
unique_rows = insurance_claims_freq.drop_duplicates(subset=sub).copy()

#%%
#unique_rows['DriverBirthDate'] = generate_unique_birthdates(unique_rows, 'DrivAge')
unique_rows['DriverBirthDate'] = unique_rows["DrivAge"].apply(random_birthdate_from_age)

#%%
ssub = sub + ['DriverBirthDate']
insurance_claims_freq = insurance_claims_freq.merge(unique_rows[ssub], on=sub, how='left')

#%%
insurance_claims_freq = insurance_claims_freq.drop(columns=["Exposure", "DrivAge"])
insurance_claims_freq.head()

#%%
# Write insurance_claims_freq
insurance_claims_freq.to_csv(url_new, index=False)