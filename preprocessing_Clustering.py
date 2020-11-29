import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from collections import defaultdict

#remove total and normalise data

df= pd.read_csv("District_wise_crimes_committed_against_women_2001_2012.csv")
df.drop(['Dowry Deaths', 'Assault on women with intent to outrage her modesty', 'Insult to modesty of Women', 'Cruelty by Husband or his Relatives', 'Importation of Girls'], axis=1, inplace=True)
df = df[df.DISTRICT != 'TOTAL']
df['Rape+Kidnap'] = df['Rape'] + df['Kidnapping and Abduction'] 

#'DELHI UT TOTAL': 19000000, 

urban = {
    'MUMBAI': 18400000, 
    'MUMBAI COMMR.': 18400000, 
    'CHENNAI': 7090000, 
    'KOLKATA': 14900000, 
    'BANGALORE COMMR.': 8430000, 
    'HYDERABAD CITY': 6810000, 
    'PATNA': 2050000, 
    'BHOPAL': 1800000, 
    'JAIPUR': 3070000, 
    'AHMEDABAD COMMR.': 8059441, 
    'PUNE COMMR.': 3120000, 
    'SURAT COMMR.': 4460000, 
    'NAGPUR COMMR.': 2410000, 
    'KANPUR NAGAR': 2920000
}

rural = {
    'CHITTORGARH': 154000, 
    'BHILWARA': 370000, 
    'BAREILLY': 1255000, 
    'DURG': 1192000, 
    'KOTA': 1387000,
    'SAGAR': 370000, 
    'KHIRI': 152000, 
    'SAGUJA': 2360000, 
    'AGRA': 1590000, 
    'BARAN': 122000, 
    'MIDNAPUR': 170000,
    'DARANG': 928000,
    'ALIGARH': 874000,
    'SONITPUR': 1920000,
    'UDAIPUR': 451000
}

df['Urban'] = 0
df['Population'] = 0
for i, row in df.iterrows():
    if not (row['DISTRICT'] in urban or row['DISTRICT'] in rural):
        df = df.drop(i)
    else:
        if row['DISTRICT'] in urban:
            df.loc[i, 'Urban'] = 1
            df.loc[i, 'Population'] = urban[row['DISTRICT']]
        else:
            df.loc[i, 'Urban'] = 0
            df.loc[i, 'Population'] = rural[row['DISTRICT']]

df['crimes/population'] = df['Rape+Kidnap']/df['Population']
df['Rape'] = df['Rape']/df['Population']
df['Kidnapping and Abduction'] = df['Kidnapping and Abduction']/df['Population']
df = df.sort_values(['crimes/population'], ascending = [False])
df = df.loc[df['Year'] == 2011]
print(df)
#df.to_csv("processed_Clustering.csv")
