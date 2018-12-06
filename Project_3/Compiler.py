from tkinter import *
from BlackjackGui import *
import Poker as Pk



def main():

    root = Tk()
    #blackjack = BJ()
    #BLKJK = Application(master = root)
    root.geometry("300x300")

    welcome = Label(root, text= "Casino 3.14")
    welcome.pack()

    welcome2 = Label(root, text="Select a Game you want to play")
    welcome2.pack()

    
    BLKJK = Application(master = root)
    #Blackjack = Button(root,text="Blackjack",command= lambda: [root.destroy(),BLKJK.creategame()])
    #Blackjack.pack()

    
    Poker = Button(root, text="Click here to Poker", command= lambda: [Pk.Game()])
    Poker.pack()


    War = Button(root, text="War", command= lambda: [root.destroy()])
    War.pack()

main()
