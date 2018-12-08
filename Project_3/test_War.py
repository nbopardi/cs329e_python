import unittest
from War import *

class testCard(unittest.TestCase):
	
	def testCardCreation(self):
		x = Card("D",14)
		self.assertEqual(x.rank, 14)
		self.assertEqual(x.suit, "D")

class testDeck(unittest.TestCase):

	def testDeckCreaton(self):
		deck = Deck()
		self.assertEqual(str(deck.cardList[0]), "2c")

	def testDeckShuffle(self):
		deck1 = Deck()
		deck1.shuffle()
		self.assertEqual(str(deck1.cardList[0]), "jh")

	def testDeckDealOne(self):
		deck2 = Deck()
		player = Player()
		deck2.dealOne(player)
		self.assertEqual(str(deck2.cardList[0]), "3c")

class testPlayer(unittest.TestCase):

	def testPlayerCreation(self):
		player = Player()
		self.assertEqual(player.hand, [])
		self.assertEqual(player.handTotal, 0)
		self.assertEqual(player.playerName, "Player 2")


if __name__ == '__main__':
    unittest.main()