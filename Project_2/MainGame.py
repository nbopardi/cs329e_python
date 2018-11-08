from tkinter import *
import pandas as pd
from PIL import Image, ImageTk


class Question():
    def __init__(self, image, question, options, answer):
        self.image = image
        self.question = question
        self.options = options
        self.answer = answer

class Player():

    def __init__(self, name):
        self.playerName = name
        self.pointValue = 0

    def addPoints(self, pointsEarned):
        self.pointValue = self.pointValue + pointsEarned
        if self.pointValue < 0:
            self.pointValue = 0

    def getPointValue(self):
        return self.pointValue

    def getName(self):
        return self.playerName

def questionWindow(question,questionCounter,user):

    questionWindow = Tk()
    questionWindow.geometry("1000x1000")

    title_question = Label(questionWindow, text=question.question)
    title_question.pack()

    image = Image.open(question.image)
    photo = ImageTk.PhotoImage(image)
    title_image = Label(questionWindow, image=photo)
    title_image.pack()
    title_image.image = photo

    option1 = Button(questionWindow, text=question.options[0],command=lambda: [questionWindow.destroy(),verifyAnswer(question.options[0],question.answer,user),engine(questionCounter+1,user)])
    option1.pack()
    option2 = Button(questionWindow, text=question.options[1],command=lambda: [questionWindow.destroy(),verifyAnswer(question.options[1],question.answer,user),engine(questionCounter+1,user)])
    option2.pack()
    option3 = Button(questionWindow, text=question.options[2],command=lambda: [questionWindow.destroy(),verifyAnswer(question.options[2],question.answer,user),engine(questionCounter+1,user)])
    option3.pack()
    option4 = Button(questionWindow, text=question.options[3],command=lambda: [questionWindow.destroy(),verifyAnswer(question.options[3],question.answer,user),engine(questionCounter+1,user)])
    option4.pack()

    questionWindow.mainloop()

def readInCSV(questionCounter):
    #this part keeps track of the Question number
    print('QUESTION ', questionCounter)

    #this part reads the CSV file
    df = pd.read_csv('meme.csv')

    #this part takes out the arguments needed from the CSV
    image = df.at[questionCounter, "Image Name"]
    question = df.at[questionCounter, "Question"]
    options = [df.at[questionCounter, "Answer 1"], df.at[questionCounter, "Answer 2"],df.at[questionCounter, "Answer 3"], df.at[questionCounter, "Answer 4"]]
    answer = df.at[questionCounter, "Correct Answer"]

    #this part takes the variables and generates a Question Object and Question Window
    testQ = Question(image, question, options, answer)
    return testQ

def engine(questionCounter, user):

    if (questionCounter<4):
        question = readInCSV(questionCounter)
        questionWindow(question,questionCounter,user)
    else:
        close = Tk()
        close.geometry("1000x1000")

        thanks = Label (close, text="Thanks for Playing")
        thanks.pack()

        pointDisplay = Label(close, text="Congrats " + user.getName() + " you scored " + str(user.getPointValue()) + " points!")
        pointDisplay.pack()

        quit = Button (close,text="Quit", command=lambda:[close.destroy()])
        quit.pack()

        close.mainloop()

def verifyAnswer(option,answer,user):
    if (option == answer):
        user.addPoints(1)

        pointDisplay = Tk()
        pointDisplay.geometry("1000x1000")

        finish = Label(pointDisplay, text= "Correct! You have " + str(user.getPointValue()) + " points!")
        finish.pack()

        nextButton = Button(text="Next", command=lambda: [pointDisplay.destroy()])
        nextButton.pack()

        pointDisplay.mainloop()

    else:
        pointDisplay = Tk()
        pointDisplay.geometry("1000x1000")

        finish = Label(pointDisplay, text="Incorrect! You have" + str(user.getPointValue()) + " points!")
        finish.pack()

        nextButton = Button(text="Next", command=lambda: [pointDisplay.destroy()])
        nextButton.pack()

        pointDisplay.mainloop()


def main():

    opener = Tk()
    opener.geometry("1000x1000")

    welcome = Label(opener, text= "Welcome to Meme Questionnaire!")
    welcome.pack()

    welcome2 = Label(opener, text="Please Enter Your Name and Press Start!")
    welcome2.pack()

    user = Player("Hamza")

    start = Button(opener,text="Start",command= lambda: [opener.destroy(),engine(0,user)])
    start.pack()

    opener.mainloop()

main()
