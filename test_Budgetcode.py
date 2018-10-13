import unittest
from Budgetcode import *

class sumunittest(unittest.TestCase):

    def test_summing(self):
        self.assertEqual(sumitems(),805.5)
