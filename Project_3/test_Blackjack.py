import unittest
from Blackjack import *

class testCard(unittest.TestCase):

	def testPointValue(self):
		card1 = Card("2", "C")
		self.assertEqual(card1.pointValue(), 2)


class testPlayer(unittest.TestCase):

	def testPlayerCreation(self):
		p = Player("Q")
		# test player getName
		self.assertEqual(p.getName(), "Q")
		# test that hand is initially empty
		self.assertEqual(p.hand, [])
		self.assertEqual(p.handTotal, 0)

	def testUpdateHandTotal(self):
		p1 = Player("T")
		d = Deck()
		d.dealOne(p1)
		p1.updateHandTotal()
		self.assertEqual(p1.handTotal, 2)


class testDeck(unittest.TestCase):
	
	def testDeckCreation(self):
		d = Deck()
		# test that the deck has been properly created
		self.assertIn('2C', str(d))
	def testDeckLength(self):
		d = Deck()
		self.assertEqual(len(d.cardList), 52)

	def testShuffle(self):
		d1 = Deck()
		d2 = Deck()
		self.assertEqual(str(d1), str(d2))
		d2.shuffle()
		self.assertIsNot(str(d1), str(d2))

	def testDealOne(self):
		p1 = Player("J")
		d3 = Deck()
		d3.dealOne(p1)
		self.assertEqual(str(p1.hand[0]), "2C")



if __name__ == '__main__':
    unittest.main()
