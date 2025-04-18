import pandas as pd

a = pd.Series([1, 2, 3, 4, 5])

b = pd.Series([1, 1, 2, 3, 5])

a = a**2

b = b**2

sum_of_squares = a + b

root_of_squares = sum_of_squares**0.5
