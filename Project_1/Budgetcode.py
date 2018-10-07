import pandas as pd
import unittest

df = pd.read_csv('budget.csv')

print(df)

x = df.describe()

#print(x)

y = df["Date"]

#print(y)

z = df["Ammount"]

class sumunittest(unittest.TestCase):

    def test_summing(self):
        self.assertEqual(sumitems(),805.5)

def sumitems():
    total = 0.0 
    for items in z:
        length = len(items)
        sObject = slice(1,length)
        numerical = items[sObject]
        total += float(numerical)
    
    return(total)



def main():

    x = sumitems()
    print(x)
    
main()

unittest.main()
