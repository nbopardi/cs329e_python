import tkinter as tk

# select number of players
# cycle through players
# vote on which answer choice is the best
# select winner and award point value
# give winner the chance to answer multiple choice question for bonus points
# first to 10 points wins (2 for caption, 1 for mc)

# Player class


def start():
    main = tk.Tk()
    main.geometry("200x200")
    user = Player("Joe")




    gamestart = tk.Button( main,text="Press to Play", command= lambda: [game(user)])
    # addUser.place(x = 80, y = 30)
    gamestart.grid(row=2,column=0)



def game(user):
    print("hi")
    question()
        


    
    
    
def main():

    start()

main()
