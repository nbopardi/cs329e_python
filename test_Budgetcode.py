import unittest
from Budgetcode import *

class sumunittest(unittest.TestCase):

    def test_summing(self):
        self.assertEqual(sumitems(),805.5)
    def test_newexpense(self):
        global price
        global date
        global category
        global df
        self.assertNotEqual(price, None)
        self.assertNotEqual(category, None)
        self.assertNotEqual(date, None)
        self.assertIn(category, str(df["type"]))
        self.assertIn(price, str(df["Ammount"]))
        self.assertIn(date, str(df["Date"]))
        
    def test_graph(self):
        cumsum = timeseries()
        temp = cumsum[0]

        for x in range(1,len(cumsum)):
            self.assertTrue(cumsum[x-1]>temp)
            temp = cumsum[x]
