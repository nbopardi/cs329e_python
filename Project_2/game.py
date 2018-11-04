import tkinter as tk
import pandas as pd
from QuizShow import *
from Player import *

questionCounter = 0

def readInCSV(title):
	df = pd.read_csv(title)
	return df

def start(master):

	user = Player("Joe")

	gamestart = tk.Button(master,text="Press to Play", command= lambda: [game(user)])
	gamestart.pack()

	master.mainloop()


def game(user):
	global questionCounter
	print('QUESTION ', questionCounter)

	df = readInCSV('meme.csv')

	image = df.at[questionCounter, "Image Name"]
	question = df.at[questionCounter, "Question"]
	options = [df.at[questionCounter, "Answer 1"],df.at[questionCounter, "Answer 2"],df.at[questionCounter, "Answer 3"],df.at[questionCounter, "Answer 4"]]
	answer = df.at[questionCounter, "Correct Answer"]

	testQ = Question(image, question, options, answer)

	questionWindow(testQ, user)

	questionCounter = questionCounter + 1

	if questionCounter >= 3: # debug: remove for final release
		questionCounter = 0



def main():
	root = tk.Tk()
	root.geometry("200x200")
	start(root)

main()