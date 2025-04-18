import pandas as pd

penguins = pd.read_csv('penguins.csv')

print(penguins.isna().sum())

percent_missing_by_row = penguins.isna().mean(axis=1) * 100

sorted_missing = percent_missing_by_row.sort_values(ascending=False)
