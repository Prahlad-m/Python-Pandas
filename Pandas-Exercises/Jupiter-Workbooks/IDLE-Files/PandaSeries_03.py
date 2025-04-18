import pandas as pd

vegetables = pd.Series(["Onion", "cucumber", "Carrot", "squash", "Potato", "Asparagus", "kale", "Broccoli", "spinach"])

vegetables = vegetables.str.lower()

vegetables = vegetables.sort_values()

print(vegetables[vegetables.str.startswith(("a","e","i","o","u"))])

print(vegetables[vegetables.str.count("[aeiou]")==2])

prices = pd.Series(["$2.99", "$1,200.25", "$5.99", "$2,350.00"])

prices = (prices.str.replace("$","")).str.replace(",","")

prices = prices.astype(float)

prices = prices * 0.9
