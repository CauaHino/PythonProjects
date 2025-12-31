import pandas as pd

df = pd.read_csv("data.csv")

# Filtering Pokemon

tall_pokemon = df[df['Height'] >= 2.0]
heavy_pokemon = df[df['Weight'] > 100.0]
legendary_pokemon = df[df['Legendary'] == True]
water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]

ff_pokemon = df[(df['Type1'] == 'Fire') & (df['Type2'] == 'Flying')]
 


# print(ff_pokemon)

# Aggregate Functions

# Whole DataFrame

# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# Single column
# print(df["Height"].mean())
# print(df['Height'].sum())
# print(df['Height'].min())
# print(df['Height'].max())
# print(df['Height'].count())

group = df.groupby('Type1')

# print(group['Height'].mean())
# print(group['Height'].sum())
# print(group['Height'].min())
# print(group['Height'].max())
# print(group['Height'].count())

# Data Cleaning

# 1. Drop irrelevant columns
# df = df.drop(columns=['Legendary', 'No'])

#2. Handle missing values
# df = df.dropna(subset=['Type2'])
# df = df.fillna({'Type2': 'None'})

# 3. Fix inconsistent data
# df['Type1'] = df['Type1'].replace({'Grass': 'GRASS', 'Fire': 'FIRE', 'Water': 'WATER'})

# 4. standardize text data
# df['Name'] = df['Name'].str.upper()

# 5. Fix data types
# df['Legendary'] = df['Legendary'].astype(bool)

# 6. Remove duplicates
df = df.drop_duplicates()


print(df.to_string())