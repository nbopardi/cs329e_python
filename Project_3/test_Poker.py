import unittest
from Poker import *

class testCard(unittest.TestCase):
	
	def testCardCreation(self):
		x = Card(14,"D")
		self.assertEqual(x.rank, 14)
		self.assertEqual(x.suit, "D")

	def testCardComparison(self):
		a = Card(11, "D")
		b = Card(10, "D")

		self.assertEqual(a == b, False)
		self.assertEqual(a != b, True)
		self.assertEqual(a < b, False)
		self.assertEqual(a <= b, False)
		self.assertEqual(a > b, True)
		self.assertEqual(a >= b, True)

class testPlayer(unittest.TestCase):

	def testCalcPoints(self):
		acards = [Card(11, "D"), Card(12, "D")]
		bcards = [Card(10, "D"), Card(9, "D")]

		player1 = Player(name = "A", cards = acards)
		player2 = Player(name = "B", cards = bcards)
		self.assertEqual(player1.calcPoints(), 23)
		self.assertEqual(player2.calcPoints(), 19)

	def testPlayerComparisons(self):
		acards = [Card(11, "D"), Card(12, "D")]
		bcards = [Card(10, "D"), Card(9, "D")]

		player1 = Player(name = "A", cards = acards)
		player2 = Player(name = "B", cards = bcards)

		self.assertEqual(player1 == player2, False)
		self.assertEqual(player1 != player2, True)
		self.assertEqual(player1 < player2, False)
		self.assertEqual(player1 <= player2, False)
		self.assertEqual(player1 > player2, True)
		self.assertEqual(player1 >= player2, True)


if __name__ == '__main__':
    unittest.main()