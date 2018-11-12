import unittest
from MainGameBACKUP import *
from Player import *

class TestQuizShow(unittest.TestCase):


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

    def testsetJudge(self):
        player4 = Player("Burkel")
        player4.setJudge(True)

        self.assertEqual(player4.isJudge,True)

    def teststoreAnswer(self):
        player5 = Player("Curkel")
        player5.storeAnswer("abc")

        self.assertEqual(player5.getAnswer(), 'abc')

    def testMCQuestion(self):
        question1 = MCQuestion("image", "question", ['a', 'b', 'c', 'd'], 'a')

        self.assertEqual(question1.image, 'image')
        self.assertEqual(question1.question, 'question')
        self.assertEqual(question1.options, ['a', 'b', 'c', 'd'], 'a')
        self.assertEqual(question1.answer, 'a')

    def testReadInCSV(self):
        question2 = readInCSV(0)

        self.assertEqual(question2.image, 'imagemc/image_1.png')
        self.assertEqual(question2.question, "What is the color of the squirrel?")
        self.assertEqual(question2.options, ["Albino", "White", "Black", "Purple"])
        self.assertEqual(question2.answer, "Albino")

    def testCreateUser(self):
        createUser("Murkel")

        self.assertEqual(playerList[0].getName(), "Murkel")

    def testDeleteUser(self):
        playerList = []
        createUser("Lurkel")
        deleteUser("Lurkel")

        self.assertEqual(playerList, [])




if __name__ == '__main__':
    unittest.main()
