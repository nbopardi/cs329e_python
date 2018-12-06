import random
import collections
from tkinter import *
from PIL import Image, ImageTk
from statistics import mode

playerList = []

class Card():

    Suits = ['H', 'S', 'C', 'D']
    Ranks = [2,3,4,5,6,7,8,9,10,11,12,13,14]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):

        if self.rank == 11:
            card = "J" + self.suit
            return card
        if self.rank == 12:
            card = "Q" + self.suit
            return card
        if self.rank == 13:
            card = "K" + self.suit
            return card
        if self.rank == 14:
            card = "A" + self.suit
            return card
        else:
            card = str(self.rank) + str(self.suit)
            return card

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.rank == other.rank)

    def __ne__(self, other):
        return (self.rank != other.rank)

    def __lt__(self, other):
        return (self.rank < other.rank)

    def __le__(self, other):
        return (self.rank <= other.rank)

    def __gt__(self, other):
        return (self.rank > other.rank)

    def __ge__(self, other):
        return (self.rank >= other.rank)

class Player():

    def __init__(self,name, cards = [], points = 0, pushers = 1):
        self.name = name
        self.cards = cards
        self.points = points
        self.pushers = pushers

    def __str__(self):
        return (self.name + " has a " + getHandName(self.pushers))

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.calcPoints() == other.calcPoints())

    def __ne__(self, other):
        return (self.calcPoints() != other.calcPoints())

    def __lt__(self, other):
        return (self.calcPoints() < other.calcPoints())

    def __le__(self, other):
        return (self.calcPoints() <= other.calcPoints())

    def __gt__(self, other):
        return (self.calcPoints() > other.calcPoints())

    def __ge__(self, other):
        return (self.calcPoints() >= other.calcPoints())

    def calcPoints(self, deck = []):
        if (len(deck) == 0):
            out = self.cards
        else:
            out = deck
        try:
            total = 0
            for x in out:
                total += x.rank
            return total
        except:
            return 0

    def isRoyalFlush(self,deck):

        total = sorted(self.cards + deck)
        spots = []
        best = []

        for x in total:
            best.append(x.suit)
            if (x.rank == 10):
                spots.append(x)
            if (x.rank == 11):
                spots.append(x)
            if (x.rank == 12):
                spots.append(x)
            if (x.rank == 13):
                spots.append(x)
            if (x.rank == 14):
                spots.append(x)

        try:
             best = mode(best)
             check = 10

             for x in spots:
                 if (x.rank == check and x.suit == best):
                     check+=1

             if (check == 15):
                self.pushers = 10
                return True
        except:
            return False

    def isStraightFlush(self,deck):

        total = cardSort(self.cards + deck)
        start = total[0].rank
        checkers = 0

        for x in total:
            if(start == x.rank):
                checkers +=1
                start += 1
            else:
                start = x.rank
                checkers = 0
            if(checkers == 5):
                self.pushers = 9
                return True
        return False

    def isFourOfAKind(self,deck):

        total = sorted(self.cards + deck)
        start = total[0].rank
        checkers = 0

        for x in total:
            if(x.rank == start):
                checkers += 1
            else:
                checkers = 0
                start = x.rank

            if(checkers>=4):
                self.pushers = 8
                return True
        return False

    def isFullHouse(self,deck):

        total = sorted(self.cards + deck)
        nums = []

        for x in total:
            nums.append(x.rank)

        counter = collections.Counter(nums)
        nums = counter.values()

        pair = False
        triad = False
        doubleTriad = False

        for x in nums:
            if x == 2:
                pair = True
            elif x == 3:
                if (triad):
                    doubleTriad = True
                else:
                    triad = True

        if (triad and pair or triad and doubleTriad):
            self.pushers = 7
            return True
        else:
            return False

    def isFlush(self,deck):

        total = cardSort(self.cards,deck,nest=True)

        for x in total:
            if(len(x)>=5):
                self.pushers = 6
                return True
        return False

    def isStraight(self,deck):

        total = sorted(self.cards + deck)
        nums = []

        for x in total:
            nums.append(x.rank)

        nums1 = nums[:5]
        check1 = 0
        nums2 = nums[1:6]
        check2 = 0
        nums3 = nums[2:7]
        check3 = 0

        for y in range(0,4):
            if (nums1[y]+1 == nums1[y+1]):
                check1 +=1
            if (nums2[y]+1 == nums2[y+1]):
                check2 +=1
            if (nums3[y]+1 == nums3[y+1]):
                check3 +=1

        if (check1==4 or check2==4 or check3==4):
            self.pushers = 5
            return True
        else:
            return False

    def isThreeOfAKind(self,deck):

        total = sorted(self.cards + deck)
        nums = []

        for x in total:
            nums.append(x.rank)

        counter = collections.Counter(nums)
        nums = counter.values()

        if (3 in nums):
            self.pushers = 4
            return True
        return False

    def isTwoPair(self,deck):

        total = sorted(self.cards + deck)
        nums = []

        for x in total:
            nums.append(x.rank)

        counter = collections.Counter(nums)
        nums = counter.values()

        firstPair = False

        for x in nums:
            if x == 2:
                if (firstPair):
                    self.pushers = 3
                    return True
                else:
                    firstPair = True
        return False


    def isOnePair(self,deck):
        total = sorted(self.cards + deck)
        nums = []

        for x in total:
            nums.append(x.rank)

        counter = collections.Counter(nums)
        nums = counter.values()

        if (2 in nums):
            self.pushers = 2
            return True
        return False

    def displayPlayer(self,deck):

        home = Tk()
        home.title(self.name+"'s Turn!")
        ww = 500  # width for the Tk root
        hh = 500  # height for the Tk root
        ws = home.winfo_screenwidth()  # width of the screen
        hs = home.winfo_screenheight()  # height of the screen
        xx = (ws / 2) - (ww/ 2)
        yy = (hs / 2) - (hh / 2)
        home.geometry('%dx%d+%d+%d' % (ww, hh, xx, yy))

        imageName = 'cards/'+ (str(self.cards[0])).lower() +'.gif'
        image = Image.open(imageName)
        photo = ImageTk.PhotoImage(image)

        imageName2 = 'cards/'+ (str(self.cards[1])).lower() + '.gif'
        image2 = Image.open(imageName2)
        photo2 = ImageTk.PhotoImage(image2)

        imageName3 = 'cards/' + (str(deck[0])).lower() + '.gif'
        image3 = Image.open(imageName3)
        photo3 = ImageTk.PhotoImage(image3)

        imageName4 = 'cards/' + (str(deck[1])).lower() + '.gif'
        image4 = Image.open(imageName4)
        photo4 = ImageTk.PhotoImage(image4)

        imageName5 = 'cards/' + (str(deck[2])).lower() + '.gif'
        image5 = Image.open(imageName5)
        photo5 = ImageTk.PhotoImage(image5)

        imageName6 = 'cards/' + (str(deck[3])).lower() + '.gif'
        image6 = Image.open(imageName6)
        photo6 = ImageTk.PhotoImage(image6)

        imageName7 = 'cards/' + (str(deck[4])).lower() + '.gif'
        image7 = Image.open(imageName7)
        photo7 = ImageTk.PhotoImage(image7)

        cardLabel = Label(home, text="<-Your Cards")
        cardLabel.grid(row=0,column=3)

        card1 = Label(home, image=photo)
        card1.grid(row=0,column=1)

        card2 = Label(home, image =photo2)
        card2.grid(row=0,column=2)

        cardLabel2 = Label(home, text="<-Table Cards")
        cardLabel2.grid(row=1, column=5)

        card3 = Label(home, image=photo3)
        card3.grid(row=1, column=0)

        card4 = Label(home, image=photo4)
        card4.grid(row=1, column=1)

        card5 = Label(home, image=photo5)
        card5.grid(row=1, column=2)

        card6 = Label(home, image=photo6)
        card6.grid(row=1, column=3)

        card7 = Label(home, image=photo7)
        card7.grid(row=1, column=4)

        endLabel = Label(home,text=str(self))
        endLabel.grid(columnspan=5,sticky=W+E)

        exit = Button(home,text="Next",command= lambda:(home.destroy()))
        exit.grid(columnspan = 5, row=3)

        home.mainloop()

class Game():


    def __init__(self,players = [], deck = [],tables = []):
        global playerList
        getPlayers()
        self.players = playerList
        self.deck = makeDeck()
        self.tables = table(self.deck)
        #self.tables = [Card(4,'H'),Card(8,'C'),Card(5,'H'),Card(6,'D'),Card(12,'S')]

        for x in self.players:

            x.cards = deal(self.deck)
            #x.cards = [Card(6,"D"),Card(14,"D")]
            x.points = x.calcPoints() + x.calcPoints(self.tables)

            x.isOnePair(self.tables)
            x.isTwoPair(self.tables)
            x.isThreeOfAKind(self.tables)
            x.isStraight(self.tables)
            x.isFlush(self.tables)
            x.isFourOfAKind(self.tables)
            x.isFullHouse(self.tables)
            x.isStraightFlush(self.tables)
            x.isRoyalFlush(self.tables)
            x.displayPlayer(self.tables)

        self.play()

    def __str__(self):
        output = ''

        for x in self.players:
            output += (str(x) + "\n")
        output += ("This is what is on the table:" + str(self.tables) + "\n")
        output += ("This is what is left in the deck: " + str(self.deck) +"\n")
        return output

    def play(self):

        output = []

        print("Here is the table: " + str(self.tables))
        pushPlace = self.players[0].pushers
        pushers = []
        for x in (self.players):
            if(x.pushers>pushPlace):
                pushPlace = x.pushers

        for y in (self.players):
            if(y.pushers == pushPlace):
                pushers.append(y)

        if (len(pushers) == 1):
            print((pushers[0].name) + " wins! They won with a " + getHandName(pushers[0].pushers))
            output.append(pushers[0])
        else:

            pointsHigh = 0
            points = []
            for x in (pushers):
                if (x.points > pointsHigh):
                    pointsHigh = x.points

            for y in (pushers):
                if (y.points == pointsHigh):
                    points.append(y)

            if(len(points)==1):
                print((points[0].name) + " wins! They won with a " + getHandName(pushers[0].pushers))
                output.append(points[0])
            else:
                for z in points:
                    print("There is a tie!")
                    print((z.name) + " wins! They won with a " + getHandName(pushers[0].pushers))
                    output.append(z)

        for x in output:
            win = Tk()
            win.title(x.name+" wins!")
            ww = 500  # width for the Tk root
            hh = 500  # height for the Tk root
            ws = win.winfo_screenwidth()  # width of the screen
            hs = win.winfo_screenheight()  # height of the screen
            xx = (ws / 2) - (ww / 2)
            yy = (hs / 2) - (hh / 2)
            win.geometry('%dx%d+%d+%d' % (ww, hh, xx, yy))

            winLabel = Label(win, text=("" + x.name + " wins! They won with a " + getHandName(x.pushers)))
            winLabel.grid(row=0, sticky=N + E + S + W)

            endGame = Button(win,text="End Game",command=lambda:win.destroy())
            endGame.grid(row=1)

            win.mainloop()


def cardSort(deck1 = [], deck2 = [],nest = False):

    total = deck1 + deck2

    hearts = []
    spades = []
    clubs = []
    diamonds = []

    for x in total:
        if x.suit == "H":
            hearts.append(x)
        if x.suit == "S":
            spades.append(x)
        if x.suit == "C":
            clubs.append(x)
        if x.suit == "D":
            diamonds.append(x)


    hearts = sorted(hearts)
    clubs = sorted(clubs)
    spades = sorted(spades)
    diamonds = sorted(diamonds)

    if (nest):
        return [hearts,clubs,spades,diamonds]
    else:
        return hearts + clubs + spades + diamonds

def getPlayers():

    master = Tk()
    master.title("Select Amount of Players")
    ww = 500  # width for the Tk root
    hh = 500  # height for the Tk root
    ws = master.winfo_screenwidth()  # width of the screen
    hs = master.winfo_screenheight()  # height of the screen
    xx = (ws / 2) - (ww / 2)
    yy = (hs / 2) - (hh / 2)
    master.geometry('%dx%d+%d+%d' % (ww, hh, xx, yy))

    variable = StringVar(master)
    variable.set(2)  # default value

    select = OptionMenu(master,variable,2,3,4,5,6)
    select.pack()

    next = Button(master,text="Select Amount of Players",command= lambda: (master.destroy(),getNames(variable.get())))
    next.pack()

    master.mainloop()

def getNames(n):

    global playerlist

    n = int(n)

    for x in range(n):
        masterbait = Tk()
        masterbait.title("Enter Player")
        ww = 500  # width for the Tk root
        hh = 500  # height for the Tk root
        ws = masterbait.winfo_screenwidth()  # width of the screen
        hs = masterbait.winfo_screenheight()  # height of the screen
        xx = (ws / 2) - (ww / 2)
        yy = (hs / 2) - (hh / 2)
        masterbait.geometry('%dx%d+%d+%d' % (ww, hh, xx, yy))

        ask = Label(masterbait, text="Enter Player" +str(x+1)+ "'s Name")
        ask.pack()

        name = Entry(masterbait, width=50)
        name.pack()

        next = Button(masterbait,text="Submit Player",command= lambda: (playerList.append(Player(name.get())),masterbait.destroy()))
        next.pack()

        masterbait.mainloop()

def makeDeck():

    output = []

    for x in range(len(Card.Suits)):
        for y in range(len(Card.Ranks)):
            output.append(Card(Card.Ranks[y],Card.Suits[x]))
    random.shuffle(output)
    return output

def deal(deck):

    output = []
    for x in range(2):
        output.append(deck.pop())
    return sorted(output)

def table(deck):

    output = []
    for x in range(5):
        deck.pop()
        output.append(deck.pop())
    return output

def getHandName(x):
    hands = ["","High Card","One Pair","Two Pair","Three of a Kind","Straight","Flush","Full House","Four of a Kind","Straight Flush","Royal Flush"]
    return hands[x]

def main():

    a = Game()
    print(a)

main()
