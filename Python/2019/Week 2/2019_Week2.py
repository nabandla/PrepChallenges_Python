import pandas as pd
import re
df = pd.read_excel(r'Week Two Input.xlsx')
df = df.dropna()
df = df[df['City'] != "City"]
df['City'] = df['City'].apply(lambda x: 'Edinburgh' if re.match(r'.*gh$',x) else 'London')
df['Header'] = df['Metric']+"-"+df['Measure']
df['Date'] = df['Date'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
df = df.pivot(index=['City', 'Date'], columns='Header', values='Value')
print(df.to_string())