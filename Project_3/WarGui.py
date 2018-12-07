import random
from PIL import Image, ImageTk
import tkinter as tk


#  Creates Player class w/ empty list and name
class Player:
    numberOfPlayers = 0
    def __init__(self):
        Player.numberOfPlayers += 1
        self.hand = []
        self.handTotal = 0
        self.playerName = "Player " + str(Player.numberOfPlayers)


#  Prints an instance of Player's hand in rows of 13
    def __str__(self):
        count = 0
        holder = " "
        for i in self.hand:
            if count == 12:
                holder = holder + '{:>3}'.format(str(i)) + "\n "
                count = 0
            else:
                holder = holder + '{:>3}'.format(str(i)) + " "
                count += 1
        return holder







#  Creates Card class that hold the abreviated suit and rank/number
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return str(self.rank) + str(self.suit)






#  Creates Deck class with a loop creating all 52 cards
class Deck:
    def __init__(self):
        self.cardList = []
        for i in range(0,4):
            for j in range(2,15):
                if j == 11:
                    value = "J"
                elif j == 12:
                    value = "Q"
                elif j == 13:
                    value = "K"
                elif j == 14:
                    value = "A"
                else:
                    value = j
                if i == 0:
                    suit = "C"
                elif i == 1:
                    suit = "D"
                elif i == 2:
                    suit = "H"
                else:
                    suit = "S"
                self.cardList.append(Card(suit,value))


#  Prints full deck in rows of 13
    def __str__(self):
        count = 0
        holder = " "
        for i in self.cardList:
            if count == 12:
                holder = holder + '{:>3}'.format(str(i)) + "\n "
                count = 0
            else:
                holder = holder + '{:>3}'.format(str(i)) + " "
                count += 1
        return holder


#  Shuffles list in accordance to seed number
    def shuffle(self):
        random.seed(15)
        random.shuffle(self.cardList)


#  Takes the top card off the deck of cards and places it into the hand of the player
    def dealOne(self, player):
        player.hand.append(self.cardList.pop(0))
        player.handTotal += 1






#  Function with all of War's logic - comparing played cards and declaring war if equal
def playGame(deck, player1, player2):
    print("\n\nInitial hands:")
    print(player1.playerName + ":\n" + str(player1) + "\n")
    print(player2.playerName + ":\n" + str(player2))
    p1Discard = []
    p2Discard = []
    roundCounter = 1
    

#  Creates a Dictionary to refer to when comparing values that are not Numbers (ex: J,Q,K,A)
    valueFinder = {
                "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5,
                "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10,
                "J" : 11, "Q" : 12, "K" : 13, "A" : 14, "0" : 0
        }
    previousTie = False
    helperCalled = False
    whoNeedsHelp = 0
    player1CardHelper = Card("N", 0)
    player2CardHelper = Card("N", 0)
#  Cycles through play actions until either player runs out of cards
    while len(player1.hand) > 0 and len(player2.hand) > 0:

        if not previousTie and not helperCalled: #  Checks if last cards played resulted in a tie - if so then don't pull new cards (already been pulled)
            print("\n\nROUND " + str(roundCounter) + ":")
            player1Card = player1.hand.pop(0)
            player2Card = player2.hand.pop(0)

            print("Player 1 plays:\t" + '{:>3}'.format(str(player1Card)) )
            print("Player 2 plays:\t" + '{:>3}'.format(str(player2Card))+"\n")

            
            
 
#  Compares values of the 2 played cards
        if int(valueFinder[str(player1Card.rank)]) + int(valueFinder[str(player1CardHelper.rank)]) > int(valueFinder[str(player2Card.rank)]) + int(valueFinder[str(player2CardHelper.rank)]):
            print("Player 1 wins round " + str(roundCounter) + ":" + '{:>4}'.format(str(player1Card)) + " >" + '{:>4}'.format(str(player2Card)) + "\n")
            if helperCalled and not previousTie:
                print(str(player1Card) + "+" + str(player1CardHelper) + " VS " + str(player2Card) + "+" + str(player2CardHelper) + "\n")
            if len(player2.hand) > 0 and not previousTie and not helperCalled:
                activateHelper = input("Does the loser want help? [y] or [n]")
                if activateHelper == "y":
                    whoNeedsHelp = 2
                    helperCalled = True
                    print("*GIVES EXTRA CARD*")
                    player2CardHelper = player2.hand.pop(0)
                    print(player2CardHelper)
                    input("PRESS ENTER")
                    continue
            
            
            
            if previousTie: #  If this comparision is a continuation of a tie then all the cards played need to be picked up
                
                recap(player1, player2)
                print("---------------BEFORE CASHIN------------------")
                cashIn(player1, p1Discard, p2Discard)
                recap(player1, player2)
                print("---------------AFTER CASHIN------------------")
                if helperCalled:
                    if whoNeedsHelp == 1:
                        player1.hand.append(player1CardHelper)
                    elif whoNeedsHelp == 2:
                        player1.hand.append(player2CardHelper)
                helperCalled = False
                player1CardHelper = Card("N",0)
                player2CardHelper = Card("S",0)
            else:
                player1.hand.append(player1Card)
                player1.hand.append(player2Card)
                if helperCalled:
                    print("APPENDED HELPER CARD")
                    if whoNeedsHelp == 1:
                        player1.hand.append(player1CardHelper)
                    elif whoNeedsHelp == 2:
                        player1.hand.append(player2CardHelper)
                    helperCalled = False
                    player2CardHelper = Card("N",0)
                    player1CardHelper = Card("S",0)
                    
            previousTie = False
            roundCounter += 1
            recap(player1, player2)

        elif int(valueFinder[str(player1Card.rank)]) + int(valueFinder[str(player1CardHelper.rank)]) < int(valueFinder[str(player2Card.rank)]) + int(valueFinder[str(player2CardHelper.rank)]):
            print("Player 2 wins round " + str(roundCounter) + ":" + '{:>4}'.format(str(player2Card)) + " >" + '{:>4}'.format(str(player1Card)) + "\n")
            if helperCalled and not previousTie:
                print(str(player1Card) + "+" + str(player1CardHelper) + " VS " + str(player2Card) + "+" + str(player2CardHelper) + "\n")
            if len(player1.hand) > 0 and not previousTie and not helperCalled:
                activateHelper = input("Does the loser want help? [y] or [n]")
                if activateHelper == "y":
                    helperCalled = True
                    whoNeedsHelp = 1
                    print("*GIVES EXTRA CARD*")
                    player1CardHelper = player1.hand.pop(0)
                    print(player1CardHelper)
                    input("PRESS ENTER")
                    continue

                
            
            if previousTie:
                cashIn(player2, p1Discard, p2Discard)
                if helperCalled:
                    if whoNeedsHelp == 1:
                        player2.hand.append(player1CardHelper)
                    elif whoNeedsHelp == 2:
                        player2.hand.append(player2CardHelper)
                helperCalled = False
                player1CardHelper = Card("N",0)
                player2CardHelper = Card("S",0)
            else:
                player2.hand.append(player1Card)
                player2.hand.append(player2Card)
                if helperCalled:
                    print("APPENDED HELPER CARD")
                    if whoNeedsHelp == 1:
                        player2.hand.append(player1CardHelper)
                    elif whoNeedsHelp == 2:
                        player2.hand.append(player2CardHelper)
                    helperCalled = False
                    player1CardHelper = Card("N",0)
                    player2CardHelper = Card("S",0)
                    
            previousTie = False
            roundCounter += 1
            recap(player1, player2)

#  If there's a tie - check if both players can tribute 3 cards for the continuation of the round
        else:
            print("War starts:" + '{:>4}'.format(str(player1Card)) + " =" + '{:>4}'.format(str(player2Card)))
            if len(player1.hand) < 5 or len(player2.hand) < 5:
                break

#  Save the cards tributed to seperate lists for later
            if not previousTie:
                p1Discard.append(player1Card)
                p2Discard.append(player2Card)
#  3 cards from each player are tributed

            for i in range(0,3):
                print(player1.playerName + " puts" + '{:>4}'.format(str(player1.hand[0])) + " face down")
                p1Discard.append(player1.hand.pop(0))
                print(player2.playerName + " puts" + '{:>4}'.format(str(player2.hand[0])) + " face down")
                p2Discard.append(player2.hand.pop(0))
                
            print(player1.playerName + " puts" + '{:>4}'.format(str(player1.hand[0])) + " face up")
            player1Card = player1.hand.pop(0)
            p1Discard.append(player1Card)
            print(player2.playerName + " puts" + '{:>4}'.format(str(player2.hand[0])) + " face up\n")
            player2Card = player2.hand.pop(0)
            p2Discard.append(player2Card)
            previousTie = True
            
            
#  Function that prints both players' hands
def recap(player1, player2):
    print("Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:")
    print(player1)
    print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:")
    print(player2)

#  Function that adds all the played cards to a player
def cashIn(player, winnings1, winnings2):
    player.hand.extend(winnings1)
    player.hand.extend(winnings2)
    del winnings1[:]
    del winnings2[:]


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

# Sets up the buttons for the game suite
    def create_widgets(self):

        self.playBlackJack = tk.Button(self)
        self.playBlackJack["text"] = "Click to play War"
        self.playBlackJack["command"] = self.createGame()
        self.playBlackJack.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")

# def main():
    def createGame(self):
        deck = Deck()               # create a deck of 52 cards called "cardDeck"
        print("Initial deck:")
        print(deck)                 # print the deck so we can see that you built it correctly

        random.seed(15)                 # leave this in for grading purposes
        deck.shuffle()              # shuffle the deck
        print("Shuffled deck:")
        print(deck)                 # print the deck so we can see that your shuffle worked

        player1 = Player()              # create a player
        player2 = Player()              # create another player

        for i in range(26):             # deal 26 cards to each player, one at
           deck.dealOne(player1)    # a time, alternating between players
           deck.dealOne(player2)


        top = tk.Toplevel()
        top.geometry("1000x1000")

#---------------------------------------------------------------------------------------

        # Contains all the cards for player 1
        p1CardLabels = []

        p1CardLabels.append(tk.Label(top))
        p1CardLabels.append(tk.Label(top))

        # Update graphics for player 1's starting cards
        self.updateImages(player1, p1CardLabels, top, row=0)

        # Contains all the cards for player 2
        p2CardLabels = []

        p2CardLabels.append(tk.Label(top))
        p2CardLabels.append(tk.Label(top))

        # Update graphics for player 2's starting cards
        self.updateImages(player2, p2CardLabels, top, row=5)


        #---------------------------------------------------------------------------------------

        playGame(deck, player1, player2)


        if not player2.hand:
            print("\n\nGame over.  Player 1 wins!")
        else:
            print("\n\nGame over.  Player 2 wins!")

        print ("\n\nFinal hands:")
        print ("Player 1:   ")
        print (player1)                 # printing a player object should print that player's hand
        print ("\nPlayer 2:")
        print (player2)                 # one of these players will have all of the cards, the other none


    def updateImages(self, player, labels, parent, row):
        cards = str(player).split()
        # print(cards) # debug

        if len(labels) < len(cards):
            while len(labels) != len(cards):
                labels.append(tk.Label(parent))

        for i in range(0, len(cards)):
            imageName = 'cards/' + cards[i].lower() + '.gif'
            image = Image.open(imageName)
            photo = ImageTk.PhotoImage(image)

            labels[i].configure(image=photo)
            labels[i].image = photo
            labels[i].grid(row=row, column=i)
# main()


root = tk.Tk()
app = Application(master=root)
app.mainloop()

