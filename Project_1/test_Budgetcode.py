import unittest
import pandas as pd
from Budgetcode import *

df = readInCSV('budget.csv')

class testModifyEntry(unittest.TestCase):

    def testDate(self):
        #test that the date is formated correctly
        modifyEntry(df = df, row = 0, date = '10/2/2018')
        self.assertEqual(df.at[0, 'Date'], pd.to_datetime('10/02/2018', exact = False).date())
        # test that the function does not accept incorrect data types
        self.assertRaises(ValueError, modifyEntry, df = df, row = 0, date = 'n')
        
        

    def testCategory(self):
        # test that the function raises errors for an input that is a number
        self.assertRaises(TypeError, modifyEntry, df = df, row = 0, category = 5)
        # test that the function raises errors for an input that is a string with numbers
        self.assertRaises(TypeError, modifyEntry, df = df, row = 0, category = 'ab#5')
        # test that the function raises errors for an input that is an empty string
        self.assertRaises(TypeError, modifyEntry, df = df, row = 0, category = '')
        # test that the category is properly changed
        modifyEntry(df = df, row = 0, category = 'Food')
        self.assertEqual(df.at[0, 'type'], 'Food')
        

    def testAmount(self):
        # test that strings cannot be put into amount
        self.assertRaises(ValueError, modifyEntry, df = df, row = 0, amount = 'n')
        # test that negative numbers cannot be put into amount
        self.assertRaises(ValueError, modifyEntry, df = df, row = 0, amount = -5)
        # test that numbers are properly changed and formated
        modifyEntry(df = df, row = 0, amount = 5)
        self.assertEqual(df.at[0, 'Ammount'], '$5.00')

class sumunittest(unittest.TestCase):

    # Test to make sure the sum of the dataframe's values are working
    def test_summing(self):
        self.assertEqual(sumitems(df),2578) # hard coded value for the original csv

    def test_newexpense(self):
        # This is tested by making sure testModifyEntry works correctly
        pass
    
    # Test to make sure the list of cumulative sums used to make the graph is correctly ordered
    def test_graph(self):
        cumsum = timeseries()
        temp = cumsum[0]

        for x in range(1,len(cumsum)):
            self.assertTrue(cumsum[x-1]>=temp)
            temp = cumsum[x]

class testDeleteRowEntry(unittest.TestCase):

    # test that a row is properly deleted
    def testDeleteRow(self):

        df = pd.read_csv('budget.csv')

        secondRow = [df.at[1, "Date"], df.at[1,"type"], df.at[1,"Ammount"]]

        df = deleteRowEntry(df, row=0)

        newFirstRow = [df.at[0, "Date"], df.at[0,"type"], df.at[0,"Ammount"]]

        self.assertEqual(secondRow, newFirstRow)

if __name__ == '__main__':
    unittest.main()
