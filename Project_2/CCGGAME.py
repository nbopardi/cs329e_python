
from tkinter import *
import pandas as pd
from Player import *
from PIL import Image, ImageTk

class FQuestion():
    def __init__(self, image):

        self.image = image
        self.options = []


def readInMainCSV():


    #this part reads the CSV file
    df = pd.read_csv('meme.csv')

    #this part takes out the arguments needed from the CSV
    image = df.at[0, "Image Name"]

    #this part takes the variables and generates a Question Object and Question Window
    testFQ = FQuestion(image)

    return testFQ


def JudgesPage(question):

    questionWindow = Tk()
    questionWindow.geometry("1000x1000")

    title_question = Label(questionWindow, text = "MEME this")
    title_question.pack()

    image = Image.open(question.image)
    photo = ImageTk.PhotoImage(image)
    title_image = Label(questionWindow, image=photo)
    title_image.pack()
    title_image.image = photo


    a = OptionMenu(questionWindow,*returnCaptions(PlayerList))

    questionWindow.mainloop()

def returnCaptions(objectList):
    captions =[]
    for x in objectList:
        people.append(x.getCaption())
    return captions
def main():
    FQuestion = readInMainCSV()
    questionWindow(FQuestion)

main()
