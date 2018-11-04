import unittest
from QuizShow import *
from Player import *

class TestQuizShow(unittest.TestCase):


    def testQuestionObjects(self):
        question1 = Question("Monkey.jpg", "What does his face tell you?", ["Happy", "Sad", "Angry", "Nervous"],"Happy")
        self.assertEqual(question1.image, "Monkey.jpg")
        self.assertEqual(question1.question,"What does his face tell you?")
        self.assertEqual(question1.options, ["Happy", "Sad", "Angry", "Nervous"])
        self.assertEqual(question1.answer, "Happy")

    def testPlayerObjects(self):
        player1 = Player("Turkel")
        self.assertEqual(player1.playerName,"Turkel")
        self.assertEqual(player1.pointValue,0)

    def testaddPoints(self):
        player2 = Player("Purkel")

        player2.addPoints(2)
        self.assertEqual(player2.pointValue,2)

        player2.addPoints(-3)
        self.assertEqual(player2.pointValue,0)

    def testgetPointValue(self):
        player3 = Player("Jurkel")

        self.assertEqual(player3.getPointValue(),0)

        player3.addPoints(5)
        self.assertEqual(player3.getPointValue(),5)
