import tkinter as tk
from PIL import Image, ImageTk

class Question():
    def __init__(self,image,question,options,answer):
        self.image = image
        self.question = question
        self.options = options
        self.answer = answer

def questionWindow(question, user):

    questionWindow = tk.Toplevel()
    questionWindow.geometry("1000x1000")

    title_question = tk.Label(questionWindow, text=question.question)
    title_question.pack()

    image = Image.open(question.image)
    photo = ImageTk.PhotoImage(image)
    title_image = tk.Label(questionWindow, image = photo)
    title_image.pack()
    title_image.image = photo

    option1 = tk.Label(questionWindow,text = question.options[0])
    option1.pack()
    option2 = tk.Label(questionWindow,text = question.options[1])
    option2.pack()
    option3 = tk.Label(questionWindow,text = question.options[2])
    option3.pack()
    option4 = tk.Label(questionWindow,text = question.options[3])
    option4.pack()

    answer = tk.Entry(questionWindow)
    answer.pack()

    submitButton = tk.Button(questionWindow, text="Submit Answer", command = lambda:[verifyAnswer(answer.get(), question.answer, user), questionWindow.destroy()])
    submitButton.pack()



def verifyAnswer(enteredAnswer, correctAnswer, user):

    if enteredAnswer == correctAnswer:
        user.addPoints(1)
        print ("You got the question correct!")
        print ("Your score is now ", user.getPointValue())

    else:
        print ("You got the question wrong!")
        print ("You entered choice ", enteredAnswer, " and the correct answer is ", correctAnswer)
        print ("Your score is now ", user.getPointValue())
 
    # Define win condition 
    if user.getPointValue() >= 1:
        print (user.getName(), ' wins!')
