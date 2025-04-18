import pandas as pd

items = [
    {"item name": "USB cable", "price": "$10.99", "type": "USB C to USB C"},
    {"item name": "USB cable", "price": "$10.99", "type": "USB A to USB C"},
    {"item name": "Batteries", "price": "$9.99", "type": "AA"},
    {"item name": "Batteries", "price": "$8.99", "type": "AAA"},
    {"item name": "Mouse", "price": "$12.99", "type": "Wireless USB"},
]

df = pd.DataFrame(items)

df.rename(columns={"item name":"item_name"},inplace=True)

df["units_sold"] = [41, 113, 54, 35, 22]

df["price"] = df["price"].str.replace("$","").astype(float)

df["total_revenue"] = df["price"] * df["units_sold"]

df["total_revenue"] = df["total_revenue"].round(2)

