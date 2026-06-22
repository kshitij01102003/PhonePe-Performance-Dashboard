#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
df=pd.read_csv("PhonePe_Unfiltered_300K.csv")
df


# In[14]:


print(df.shape,"\n")
df.head()


# In[18]:


# Check Dataset Information
df.info()

print("\nMissing Values")
df.isnull().sum()

print("\nDuplicate Rows")
df.duplicated().sum()


# In[20]:


# Remove Leading and Trailing Spaces
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip()


# In[21]:


df.head()


# In[23]:


# Convert Empty Strings into NULL
df.replace('', np.nan, inplace=True)
df.replace(' ', np.nan, inplace=True)

print(df.isnull().sum())


# In[25]:


# Find Missing Values
missing = df.isnull().sum()

print(missing)


# In[26]:


# Remove Rows Having Too Many Missing Values
df = df[df.isnull().sum(axis=1) < 3]
print(df.shape)


# In[27]:


print("Before:", df.shape)
df = df.drop_duplicates()
print("After:", df.shape)


# In[30]:


# Remove Duplicate Transaction IDs
df = df.drop_duplicates(
    subset='TRANSACTION_ID',
    keep='first'
)

print(df.shape)


# In[31]:


# Convert all text to proper case.
cols = [
    'SERVICE',
    'SERVICE_TYPE',
    'PAYMENT_STATUS',
    'REASON'
]

for col in cols:
    df[col] = df[col].str.title()

print("Case Standardized")


# In[32]:


# Fix Spelling Mistakes
corrections = {

    "Moblie Recharge":"Mobile Recharge",
    "Mutul Fund":"Mutual Fund",
    "Credt Score":"Credit Score",

    "Sucessful":"Successful",

    "Recharge Bills":"Recharge_Bills",

    "Money Transfer":"Money_Transfer"

}

df.replace(corrections,inplace=True)


# In[33]:


# Remove Invalid USER_ID
df = df[
    df['USER_ID'].astype(str)
    .str.match(r'^PP\d{7}$',na=False)
]

print(df.shape)


# In[34]:


# Remove Negative and Zero Amounts
df = df[df['AMOUNT'] > 0]
print(df.shape)


# In[35]:


# Convert Date Column correctly 
df['DATE'] = pd.to_datetime(
    df['DATE'],
    errors='coerce',
    dayfirst=True
)


# In[36]:


df = df.dropna(subset=['DATE'])


# In[37]:


df = df[
    (df['DATE'] >= '2025-01-01')
    &
    (df['DATE'] <= '2025-12-31')
]


# In[40]:


df.shape


# In[41]:


# These are the bad rows because:

# Status says Successful
# Reason says Server Error or Wrong Info

df = df[
    ~(
        (df['PAYMENT_STATUS'] == 'Successful')
        &
        (df['REASON'] != 'Successful')
    )
]


# In[42]:


df.shape


# In[43]:


# Remove Invalid Service Types
valid_types = [
'To Qr Code',
'To Mobile Number',
'To Upi Id',
'To Self Account',
'Mobile Recharge',
'Fastag Recharge',
'Dth',
'Cable Tv',
'Gold Loan',
'Bike Loan',
'Car',
'Health',
'Term Life',
'Mutual Fund',
'Credit Score',
'Bike'

]

df = df[
    df['SERVICE_TYPE'].isin(valid_types)
]


# In[44]:


df.shape


# In[45]:


# removing special character
df['USER_ID'] = df['USER_ID'].str.replace(
    r'[^A-Za-z0-9]',
    '',
    regex=True
)


# In[47]:


df.shape


# In[49]:


df = df.dropna()
df.shape


# In[50]:


# sort dates
df = df.sort_values(
    by='DATE'
)


# In[51]:


df.head()


# In[55]:


df.info()


# In[56]:


df.isnull().sum()


# In[57]:


df.duplicated().sum()


# In[70]:


df.to_csv(
    r"C:\Darwin\PhonePe_Filtered.csv",
    index=False
)

print("Dataset saved successfully.")


# In[ ]:




