import random
import collections
from statistics import mode

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
        return ("This is "+ self.name + " with these cards: " + str(self.cards) + " and these many points: " + str(self.points)+" and these many pushers: " +str(self.pushers))

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


class Game():

    def __init__(self,players = [], deck = [],tables = []):
        self.players = getPlayers()
        self.deck = makeDeck()
        self.tables = table(self.deck)
        #self.tables = [Card(4,'H'),Card(8,'H'),Card(5,'H'),Card(6,'H'),Card(14,'D')]

        for x in self.players:

            x.cards = deal(self.deck)
            #x.cards = [Card(6,"D"),Card(14,"D")]
            x.points = x.calcPoints() + x.calcPoints(self.tables)

            x.isOnePair(self.tables)
            x.isTwoPair(self.tables)
            x.isThreeOfAKind(self.tables)
            x.isStraight(self.tables)
            x.isFlush(self.tables)
            x.isFullHouse(self.tables)
            x.isStraightFlush(self.tables)
            x.isRoyalFlush(self.tables)

        self.play()

    def __str__(self):
        output = ''

        for x in self.players:
            output += (str(x) + "\n")
        output += ("This is what is on the table:" + str(self.tables) + "\n")
        output += ("This is what is left in the deck: " + str(self.deck) +"\n")
        return output

    def play(self):

        """
        for x in self.players:
            print("It Is " + x.name + "'s Turn")
            input("Press Any Key To Continue")
            print("")
            print("Here Are Your Cards:" + str(x.cards))
            print("Here Is The Table:" + str(self.tables[:3]))
            print("")
            ans = str(input("Would You Like To Stay? Press n To Leave"))
            print("")
            if (ans=='n'):
                self.players.remove(x)

        for x in self.players:
            print("It Is " + x.name + "'s Turn")
            input("Press Any Key To Continue")
            print("")
            print("Here Are Your Cards:" + str(x.cards))
            print("Here Is The Table:" + str(self.tables[:4]))
            print("")
            ans = str(input("Would You Like To Stay? Press n To Leave"))
            print("")
            if (ans=='n'):
                self.players.remove(x)
        """

        print("Here is the table" + str(self.tables))

        highPush = 0

        highestPoint = 0
        highPoint = []

        winners = []

        for x in self.players:
            if(x.pushers>highPush):
                highPush = x.pushers

        for y in self.players:
            if(y.pushers == highPush):
                highPoint.append(y)

        for z in highPoint:
            if(z.points>highestPoint):
                highestPoint = z.points

        for a in highPoint:
            if(a.points==highestPoint):
                winners.append(a)

        if(len(highPoint)>1):
            print("The game is tied!")

        for x in highPoint:
            print(x.name + " Wins! They Won With A " + getHandName(x.pushers))



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

    while True:
        try:
            output = []
            num = eval(input("Enter Number of Players "))
            if (num>6):
                raise ValueError
            else:
                for x in range(num):
                    name = str(input("Enter Name of Player " + str(x+1) +" "))
                    output.append(Player(name))
                return output
        except:
            print("This input is not correct, please enter a number between 1-6")

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
