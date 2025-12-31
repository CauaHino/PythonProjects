import pandas as pd

data = {
    'Name': ['Spongebob', 'Patrick', 'Squidward', 'Mr.Krabs'],
    'Age': [20, 21, 22, 23]
}

df = pd.DataFrame(data, index=['Employee1', 'Employee2', 'Employee3', 'Employee4'])

# Add a new column
df['Job'] = ['Fry Cook', 'N/A', 'Cashier', 'Owner']

# Add a new row
new_row = pd.DataFrame([{'Name': 'Sandy', 'Age': 24, 'Job': 'Scientist'}], index=['Employee5'])
df = pd.concat([df, new_row])
print(df)