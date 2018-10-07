import pandas as pd
import unittest
import numpy

df = pd.read_csv('budget.csv')

print(df)

x = df.describe()

#print(x)

y = df["Date"]

#print(y)



def newexpense(df):
    price = input("Enter Price")
    category = input("Enter Type of Expense")

    date = input("Enter Date")
    f = open("budget.csv", "a")
    f.write('\n')
    

    df2 = pd.DataFrame(columns=['Date', 'type', 'Ammount'])
    df2.loc[0] = [date, category, price]

    df2.to_csv(f, index=False, header=False)

    f.close
    df3 = pd.read_csv('budget.csv')
    return df3
    

class sumunittest(unittest.TestCase):

    def test_summing(self):
        self.assertEqual(sumitems(),805.5)

def sumitems(df):
    z = df["Ammount"]
    total = 0.0 
    for items in z:
        length = len(items)
        sObject = slice(1,length)
        numerical = items[sObject]
        total += float(numerical)
    
    return(total)



def main():
    
    
    y = newexpense(df)
    x = sumitems(y)
    print("Sum:", x)
    
    

    
main()

unittest.main()
