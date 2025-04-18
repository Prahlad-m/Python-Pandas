import pandas as pd

penguins = pd.read_csv('penguins.csv')

penguins['bill_length_mm'] = penguins['bill_length_mm'].fillna(penguins['bill_length_mm'].mean())

penguins['bill_depth_mm'] = penguins['bill_depth_mm'].fillna(penguins['bill_depth_mm'].mean())

penguins['body_mass_g'] = penguins['body_mass_g'].fillna(penguins['body_mass_g'].mean())

print(penguins['sex'].value_counts())

penguins['sex'] = penguins['sex'].fillna(penguins['sex'].mode()[0])

print(penguins['sex'].value_counts())
