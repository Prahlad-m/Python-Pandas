import pandas as pd

mpg = pd.read_csv("mpg.csv")

#df['Category'] = df['UserID'].apply(lambda x: 'High' if x > 5 else 'Low')

mpg['is_automatic'] = mpg['trans'].str.contains('auto')

print(mpg['is_automatic'].sum())

print(str(round((mpg['class'].eq('compact').sum() / len(mpg)) * 100,2))+'%')

mpg['fuel_economy'] = mpg['cty'] * 0.55 + mpg['hwy'] * 0.43

print(mpg[mpg['fuel_economy'] > mpg['fuel_economy'].median()])

