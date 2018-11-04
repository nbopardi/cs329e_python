from tkinter import *
from PIL import Image, ImageTk

class Question():
    def __init__(self,image,question,options,answer):
        self.image = image
        self.question = question
        self.options = options
        self.answer = answer

def questionWindow(question):

    questionWindow = Tk()
    questionWindow.geometry("500x500")

    title_question = Label(questionWindow, text=question.question)
    title_question.pack()


    image = Image.open(question.image)
    photo = ImageTk.PhotoImage(image)
    title_image = Label(questionWindow, image = photo)
    title_image.pack()

    option1 = Button(questionWindow,text = question.options[0])
    option1.pack()
    option2 = Button(questionWindow,text = question.options[1])
    option2.pack()
    option3 = Button(questionWindow,text = question.options[2])
    option3.pack()
    option4 = Button(questionWindow,text = question.options[3])
    option4.pack()


    questionWindow.mainloop()


def main():

    pop = Question("Monkey.jpg","fuck",["go","fuck","yourself","bitch"],"fuck")
    questionWindow(pop)


main()

