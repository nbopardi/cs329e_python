import unittest
from QuizShow import *

class TestQuizShow(unittest.TestCase):


    def testObjects(self):
        question1 = Question("Monkey.jpg", "What does his face tell you?", ["Happy", "Sad", "Angry", "Nervous"],"Happy")
        self.assertEqual(question1.image, "Monkey.jpg")
        self.assertEqual(question1.question,"What does his face tell you?")
        self.assertEqual(question1.options, ["Happy", "Sad", "Angry", "Nervous"])
        self.assertEqual(question1.answer, "Happy")