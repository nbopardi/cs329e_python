import pandas as pd

df = pd.read_csv('budget.csv')

#print(df)

x = df.describe()

#print(x)

y = df["Date"]

#print(y)

z = df["Ammount"]

total = 0.0


for items in z:
    length = len(items)
    sObject = slice(1,length)
    numerical = items[sObject]
    total += float(numerical)
    
print(total)
end = df.tail()

print(end)

#print(z)
