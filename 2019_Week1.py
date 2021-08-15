# 2019 Week 1 Challenge
import pandas as pd
df = pd.read_csv(r'2019 Week 1.csv')
df['dateInt'] = df['When Sold Year'].astype(str) + df['When Sold Month'].astype(str).str.zfill(2) + "01"
df['Date'] = pd.to_datetime(df['dateInt'], format='%Y%m%d')
df['Total Cars Sold'] = df['Red Cars']+df['Silver Cars']+df['Black Cars']+df['Blue Cars']
print(df[['Date', 'Total Cars Sold', 'Dealership', 'Red Cars',  'Silver Cars',  'Black Cars',  'Blue Cars']].to_string())

