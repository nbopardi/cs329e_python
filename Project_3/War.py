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
        self.playerHandText = ["0n", "0n"]

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
        for i in range(0, 4):
            for j in range(2, 15):
                if j == 11:
                    value = "j"
                elif j == 12:
                    value = "q"
                elif j == 13:
                    value = "k"
                elif j == 14:
                    value = "a"
                else:
                    value = j
                if i == 0:
                    suit = "c"
                elif i == 1:
                    suit = "d"
                elif i == 2:
                    suit = "h"
                else:
                    suit = "s"
                self.cardList.append(Card(suit, value))


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









class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

        self.p1Discard = []
        self.p2Discard = []
        self.roundCounter = 1

        #  Creates a Dictionary to refer to when comparing values that are not Numbers (ex: J,Q,K,A)
        self.valueFinder = {
            "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "j": 11, "q": 12, "k": 13, "a": 14, "0": 0
        }
        self.previousTie = False
        self.helperCalled = False
        self.quitGame = False
        self.whoNeedsHelp = 0

        self.player1CardHelper = Card("n", 0)
        self.player2CardHelper = Card("n", 0)

# Sets up the buttons for the game suite
    def create_widgets(self):

        self.playWar = tk.Button(self)
        self.playWar["text"] = "Click to play War"
        self.playWar["command"] = self.createGame
        self.playWar.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")

    def updateImages(self, playerHandText, labels, parent, row):

        # print(cards) # debug

        # if len(labels) < len(cards):
        #     while len(labels) != len(cards):
        #         labels.append(tk.Label(parent))


        imageName = 'cards/' + playerHandText[0] + '.gif'
        image = Image.open(imageName)
        photo = ImageTk.PhotoImage(image)

        labels[0].configure(image=photo)
        labels[0].image = photo
        labels[0].grid(row=row, column=0)

# def main():
    def createGame(self):
        deck = Deck()               # create a deck of 52 cards called "cardDeck"

        random.seed(15)                 # leave this in for grading purposes
        deck.shuffle()              # shuffle the deck

        player1 = Player()              # create a player
        player2 = Player()              # create another player

        for i in range(26):             # deal 26 cards to each player, one at
            deck.dealOne(player1)    # a time, alternating between players
            deck.dealOne(player2)


# ---------------------------------------------------------------------------------------

        top = tk.Toplevel()
        top.geometry("1000x1000")


        # Contains all the cards for player 1
        p1CardLabels = []

        p1CardLabels.append(tk.Label(top))
        # p1CardLabels.append(tk.Label(top))

        # Update graphics for player 1's starting cards
        self.updateImages(player1.playerHandText, p1CardLabels, top, row=0)



        # Contains all the cards for player 2
        p2CardLabels = []

        p2CardLabels.append(tk.Label(top))
        # p2CardLabels.append(tk.Label(top))

        # Update graphics for player 2's starting cards
        self.updateImages(player2.playerHandText, p2CardLabels, top, row=5)



        # Button to play next round
        helperButton = tk.Button(top, text='Continue Round', command=lambda: [self.playGame(player1, player2, False, p1CardLabels, p2CardLabels, top)])
        helperButton.grid(row=0, column=5)

        # Button to add helperCard
        # if not self.previousTie and not self.helperCalled:
        #     helperButton = tk.Button(top, text='Add Helper Card to Loser', command=lambda: [self.playGame(player1, player2, True)])
        #     helperButton.grid(row=0, column=6)


        # print("\n\nInitial hands:")
        # print(player1.playerName + ":\n" + str(player1) + "\n")
        # print(player2.playerName + ":\n" + str(player2))


        #---------------------------------------------------------------------------------------

        # playGame(deck, player1, player2)

    def playGame(self, player1, player2, activateHelper, p1Labels, p2Labels, top):
        #  Function with all of War's logic - comparing played cards and declaring war if equal

        #  Cycles through play actions until either player runs out of cards
        if (len(player1.hand) > 0 and len(player2.hand) > 0) or self.quitGame:
            if not self.previousTie and not self.helperCalled:  # Checks if last cards played resulted in a tie - if so then don't pull new cards (already been pulled)
                print("\n\nROUND " + str(self.roundCounter) + ":")
                player1Card = player1.hand.pop(0)
                player2Card = player2.hand.pop(0)

                player1.playerHandText[0] = str(player1Card)
                player2.playerHandText[0] = str(player2Card)
                self.updateImages(player1.playerHandText, p1Labels, top, row=0)
                self.updateImages(player2.playerHandText, p2Labels, top, row=5)
                print("Player 1 plays:\t" + '{:>3}'.format(str(player1Card)))
                print("Player 2 plays:\t" + '{:>3}'.format(str(player2Card)) + "\n")

            if self.previousTie:
                player1Card = player1.playerHandText[0]
                player2Card = player2.playerHandText[0]

            #  Compares values of the 2 played cards
            if int(self.valueFinder[str(player1Card.rank)]) + int(self.valueFinder[str(self.player1CardHelper.rank)]) > int(self.valueFinder[str(player2Card.rank)]) + int(self.valueFinder[str(self.player2CardHelper.rank)]):
                print("Player 1 wins round " + str(self.roundCounter) + ":" + '{:>4}'.format(
                    str(player1Card)) + " >" + '{:>4}'.format(str(player2Card)) + "\n")
                if self.helperCalled and not self.previousTie:
                    print(str(player1Card) + "+" + str(self.player1CardHelper) + " VS " + str(player2Card) + "+" + str(self.player2CardHelper) + "\n")
                if len(player2.hand) > 0 and not self.previousTie and not self.helperCalled:
                    # activateHelper = input("Does the loser want help? [y] or [n]")
                    if activateHelper:
                        self.whoNeedsHelp = 2
                        self.helperCalled = True
                        print("*GIVES EXTRA CARD*")
                        self.player2CardHelper = player2.hand.pop(0)
                        player2.playerHandText[1] = self.player2CardHelper
                        print(self.player2CardHelper)
                        input("PRESS ENTER")
                        return
                        # continue

                if self.previousTie:  # If this comparision is a continuation of a tie then all the cards played need to be picked up

                    self.recap(player1, player2)
                    self.cashIn(player1, self.p1Discard, self.p2Discard)
                    self.recap(player1, player2)
                    if self.helperCalled:
                        if self.whoNeedsHelp == 1:
                            player1.hand.append(self.player1CardHelper)
                        elif self.whoNeedsHelp == 2:
                            player1.hand.append(self.player2CardHelper)
                    self.helperCalled = False
                    self.player1CardHelper = Card("n", 0)
                    self.player2CardHelper = Card("n", 0)
                else:
                    player1.hand.append(player1Card)
                    player1.hand.append(player2Card)
                    if self.helperCalled:
                        print("APPENDED HELPER CARD")
                        if self.whoNeedsHelp == 1:
                            player1.hand.append(self.player1CardHelper)
                        elif self.whoNeedsHelp == 2:
                            player1.hand.append(self.player2CardHelper)
                        self.helperCalled = False
                        self.player2CardHelper = Card("n", 0)
                        self.player1CardHelper = Card("n", 0)
                        player1.playerHandText[1] = "0n"
                        player2.playerHandText[1] = "0n"

                self.previousTie = False
                self.roundCounter += 1
                self.recap(player1, player2)

            elif int(self.valueFinder[str(player1Card.rank)]) + int(self.valueFinder[str(self.player1CardHelper.rank)]) < int(self.valueFinder[str(player2Card.rank)]) + int(self.valueFinder[str(self.player2CardHelper.rank)]):
                print("Player 2 wins round " + str(self.roundCounter) + ":" + '{:>4}'.format(
                    str(player2Card)) + " >" + '{:>4}'.format(str(player1Card)) + "\n")
                if self.helperCalled and not self.previousTie:
                    print(str(player1Card) + "+" + str(self.player1CardHelper) + " VS " + str(player2Card) + "+" + str(
                        self.player2CardHelper) + "\n")
                if len(player1.hand) > 0 and not self.previousTie and not self.helperCalled:
                    # self.activateHelper = input("Does the loser want help? [y] or [n]")
                    if activateHelper:
                        self.helperCalled = True
                        self.whoNeedsHelp = 1
                        print("*GIVES EXTRA CARD*")
                        self.player1CardHelper = player1.hand.pop(0)
                        player1.playerHandText[1] = self.player1CardHelper
                        print(self.player1CardHelper)
                        input("PRESS ENTER")
                        return
                        # continue

                if self.previousTie:
                    self.cashIn(player2, self.p1Discard, self.p2Discard)
                    if self.helperCalled:
                        if self.whoNeedsHelp == 1:
                            player2.hand.append(self.player1CardHelper)
                        elif self.whoNeedsHelp == 2:
                            player2.hand.append(self.player2CardHelper)
                    self.helperCalled = False
                    self.player1CardHelper = Card("n", 0)
                    self.player2CardHelper = Card("n", 0)
                    player1.playerHandText[1] = "0n"
                    player2.playerHandText[1] = "0n"
                else:
                    player2.hand.append(player1Card)
                    player2.hand.append(player2Card)
                    if self.helperCalled:
                        print("APPENDED HELPER CARD")
                        if self.whoNeedsHelp == 1:
                            player2.hand.append(self.player1CardHelper)
                        elif self.whoNeedsHelp == 2:
                            player2.hand.append(self.player2CardHelper)
                        self.helperCalled = False
                        self.player1CardHelper = Card("n", 0)
                        self.player2CardHelper = Card("n", 0)
                        player1.playerHandText[1] = "0n"
                        player2.playerHandText[1] = "0n"

                self.previousTie = False
                self.roundCounter += 1
                self.recap(player1, player2)

            #  If there's a tie - check if both players can tribute 3 cards for the continuation of the round
            else:
                print("War starts:" + '{:>4}'.format(str(player1Card)) + " =" + '{:>4}'.format(str(player2Card)))
                if len(player1.hand) < 5 or len(player2.hand) < 5:
                    self.quitGame = True
                    "GAAAAAAAAAAAAAAAAAAAAAAAAME OOOOOOOOOOOOOOOOVER"
                    return
                    # break

                #  Save the cards tributed to seperate lists for later
                if not self.previousTie:
                    self.p1Discard.append(player1Card)
                    self.p2Discard.append(player2Card)
                #  3 cards from each player are tributed

                for i in range(0, 3):
                    print(player1.playerName + " puts" + '{:>4}'.format(str(player1.hand[0])) + " face down")
                    self.p1Discard.append(player1.hand.pop(0))
                    print(player2.playerName + " puts" + '{:>4}'.format(str(player2.hand[0])) + " face down")
                    self.p2Discard.append(player2.hand.pop(0))

                print(player1.playerName + " puts" + '{:>4}'.format(str(player1.hand[0])) + " face up")
                player1Card = player1.hand.pop(0)
                player1.playerHandText[0] = player1Card
                self.p1Discard.append(player1Card)
                print(player2.playerName + " puts" + '{:>4}'.format(str(player2.hand[0])) + " face up\n")
                player2Card = player2.hand.pop(0)
                player2.playerHandText[0] = player2Card
                self.p2Discard.append(player2Card)
                self.previousTie = True
        else:
            print("GAME OVER")
            if not player2.hand:
                print("\n\nGame over.  Player 1 wins!")
            else:
                print("\n\nGame over.  Player 2 wins!")

            print("\n\nFinal hands:")
            print("Player 1:   ")
            print(player1)  # printing a player object should print that player's hand
            print("\nPlayer 2:")
            print(player2)  # one of these players will have all of the cards, the other none

    # Function that prints both players' hands
    def recap(self, player1, player2):
        print("Player 1 now has " + str(len(player1.hand)) + " card(s) in hand:")
        print("Player 2 now has " + str(len(player2.hand)) + " card(s) in hand:")

    #  Function that adds all the played cards to a player
    def cashIn(self, player, winnings1, winnings2):
        player.hand.extend(winnings1)
        player.hand.extend(winnings2)
        del winnings1[:]
        del winnings2[:]


# main()


root = tk.Tk()
app = Application(master=root)
app.mainloop()

