from tkinter import *
import pandas as pd
from PIL import Image, ImageTk
from Player import *


playerList = []

class MCQuestion():
    def __init__(self, image, question, options, answer):
        self.image = image
        self.question = question
        self.options = options
        self.answer = answer

def questionWindow(question,user):

    questionWindow = Toplevel()
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
    testQ = MCQuestion(image, question, options, answer)
    return testQ

def readInMainCSV(questionCounter):


    #this part reads the CSV file
    df = pd.read_csv('meme.csv')

    #this part takes out the arguments needed from the CSV
    image = df.at[questionCounter, "Image Name"]

    #this part takes the variables and generates a Question Object and Question Window
    #testFQ = FQuestion(image)

    return image
    
def engine(questionCounter, user,opener):
    
    #Who is inputting their answer
    #Who is the judge (skip their answer)
    #save each answer
    #change to display answers for judge to choose
    if len(playerList) < 3:
        print("You need at least 3 Players to play!")
        start()  
        
    else:    
        if (questionCounter<4):
            question = readInMainCSV(questionCounter) 
            question2 = readInCSV(questionCounter) 
            counter = 0
            judge = playerList[counter].setJudge(True)
            
    
            fibitchSubEngine(question,question2,0,[],judge,opener)
                

            counter += 1
            if counter >= len(playerList):
                counter = 0

            
            #JudgesPage(question,question2,opener)

            questionCounter += 1




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


    
def fibitchSubEngine(question,question2,usernum,answers,judge,opener):
    if usernum<len(playerList):
        fibitch(question,question2,usernum,answers,judge,opener)
    else:
        print(answers)
        JudgesPage(question,question2,opener)
        return answers


def fibitch(question,question2,usernum,answers,judge,opener):
    if judge == True:
        judge = False
    else:
        open = Tk()
        open.geometry("1000x1000")

        image = Image.open(question)
        photo = ImageTk.PhotoImage(image)
        title_image = Label(open,image=photo)
        title_image.pack()
        title_image = photo

        default = StringVar()
        answer = Entry(open,textvariable=default)
        answer.pack()
        default.set("")

        select = Button(open,text="Enter",command = lambda:[playerList[usernum].storeAnswer(answer.get()),answers.append(answer.get()),open.destroy(),fibitchSubEngine(question,question2,usernum+1,answers,judge,opener)])
        select.pack()

        open.mainloop()
    
def JudgesPage(question,question2,opener):

    judgeWindow = Toplevel()
    judgeWindow.geometry("1000x1000")

    title_question = Label(judgeWindow, text = "MEME this")
    title_question.pack()

    #print(question.image) # debug
    
    image = Image.open(question)
    print("1")
    photo = ImageTk.PhotoImage(image)
    print("2")
    title_image = Label(judgeWindow, image=photo)
    print("3")
    title_image.pack()
    print("4")
    title_image.image = photo
    print("g")

    variable = StringVar(judgeWindow)
    variable.set("(select caption)")
    a = OptionMenu(judgeWindow,variable,*returnCaptions(playerList))
    a.pack()
    b = Button(judgeWindow,text="Select",command= lambda: [judgeWindow.destroy(),getpersonbycaption(question2,variable.get())])
    b.pack()
    print("got past option menu")

    judgeWindow.mainloop()
def getpersonbycaption(question,caption):
    for players in playerList:
        if players.caption == caption:
               players.addPoints(1)
               questionWindow(question,players) 
        
def returnCaptions(objectList):
    captions =[]
    for x in objectList:
        captions.append(x.getAnswer())
    return captions

def verifyAnswer(option,answer,user):
    if (option == answer):
        user.addPoints(1)

        pointDisplay = Tk()
        pointDisplay.geometry("1000x1000")

        finish = Label(pointDisplay, text= "Correct! You have " + str(user.getPointValue()) + " points!")
        finish.pack()

        nextButton = Button(pointDisplay,text="Next", command=lambda: [pointDisplay.destroy()])
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

def addPlayers():

	add = Tk()
	add.geometry("500x500")
	a = Label(add,text="Player:")
	a.pack()
	p1 = Entry(add)
	p1.pack()

	e = Button(add, text = "Add Player", command = lambda: [createUser(p1.get()), add.destroy(), main()])
	e.pack()


def createUser(name):
	newPlayer = Player(name)
	print(newPlayer.getName())
	playerList.append(newPlayer)
	print(getPlayerNames(playerList))

def getPlayerNames(playerList):
	players = []
	for i in playerList:
		players.append(i.getName())
	return(players)

def deletePlayers():

	delete = Tk()
	delete.geometry("500x500")
	l = Label(delete, text="Please delete a player from the player list:")
	l.pack()
	
	b = Label(delete, text=getPlayerNames(playerList))
	b.pack()

	c = Entry(delete)
	c.pack()

	deleteButton = Button(delete, text = "Delete Player", command = lambda: [deleteUser(c.get()), delete.destroy(), main()])
	deleteButton.pack()

def deleteUser(name):
	for i in playerList:
		if i.getName() == name:
			playerList.remove(i)
	print(getPlayerNames(playerList))

def start():

    opener = Tk()
    opener.geometry("1000x1000")

    welcome = Label(opener, text= "Welcome to Meme Questionnaire!")
    welcome.pack()

    welcome2 = Label(opener, text="Press Start to Begin!")
    welcome2.pack()

    user = Player("Hamza")
    playerList.append(user)
    playerList.append(Player("Austin"))
    playerList.append(Player("Andy"))
    

    start = Button(opener,text="Start",command= lambda: [opener.destroy(),engine(0,user,opener)])
    start.pack()

    
    a = Button(opener, text="Add Player", command= lambda: [opener.destroy(), addPlayers()])
    a.pack()


    b = Button(opener, text="Delete Player", command= lambda: [opener.destroy(), deletePlayers()])
    b.pack()

    opener.mainloop() 
def main():

    start()



main()
