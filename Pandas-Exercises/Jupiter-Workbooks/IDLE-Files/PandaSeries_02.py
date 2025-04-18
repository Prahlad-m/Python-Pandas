import pandas as pd


#1
ser = range(-4, 5)
ser = pd.Series(ser)

#2
a=[]
for i in ser:
    if i == 2:
        a.append(True)
    else:
        a.append(False)

#3
b=[]
for i in ser:
    if i == 2 or i == 4:
        b.append(True)
    else:
        b.append(False)

is_positive = ser > 0
positives = ser[is_positive]

is_even = ser%2==0
evens = ser[is_even]

is_even_and_positive = is_even & is_positive
even_positives = ser[is_even_and_positive]

is_even_or_positive = is_even | is_positive
even_or_positive = ser[is_even_or_positive]

ser.loc[is_even_and_positive] = 0

is_negative = ser < 0
ser.loc[is_negative] = ser.loc[is_negative] * 20
