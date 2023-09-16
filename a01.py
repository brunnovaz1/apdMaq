import pandas as pd

df = pd.read_csv('dados4.csv')
print(df.info())
new_df = df.fillna(7, inplace = True)

print(new_df.info())