from tkinter import *
from BlackjackGui import *



def main():

    root = Tk()
    #blackjack = BJ()
    #BLKJK = Application(master = root)
    root.geometry("300x300")

    welcome = Label(root, text= "3.14")
    welcome.pack()

    welcome2 = Label(root, text="Select a Game you want to play")
    welcome2.pack()

    
    BLKJK = Application(master = root)
    #Blackjack = Button(root,text="Blackjack",command= lambda: [root.destroy(),BLKJK.creategame()])
    #Blackjack.pack()

    
    Poker = Button(root, text="Poker", command= lambda: [root.destroy()])
    Poker.pack()


    War = Button(root, text="War", command= lambda: [root.destroy()])
    War.pack()

main()
