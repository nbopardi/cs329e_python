#  File: Blackjack.py
#  Description: Plays a simplified game of Blackjack with multiple players and the computer as the dealer.

import random

# The Card class, which creates a playing card with a rank, suit, and point value for Blackjack
class Card:

	# Initializes a Card object
	# Parameter: rank - the rank, or number, for the card (ranges from ace, to king)
	# Parameter: suit - the suit of the Card, which is either clubs, diamonds, hearts, or spades
	def __init__(self, rank, suit):

		self.rank = rank # the instance variable that represents the Card's rank
		self.suit = suit # the instance varaible that represents the Card's suit
		self.value = self.pointValue() # assigns a point value to the card

	# Assigns a point value to the Card based on the rank of the Card
	def pointValue(self):

		return {

			"2": 2,
			"3": 3,
			"4": 4,
			"5": 5,
			"6": 6,
			"7": 7,
			"8": 8,
			"9": 9,
			"10": 10,
			"J": 10,
			"Q": 10,
			"K": 10,
			"A": 1
		}[self.rank]

	# Prints the rank and suit of the Card when asked to print the Card object
	# Return: the rank and suit of the Card
	def __str__(self):

		return(self.rank + self.suit)

# The Deck class, which creates a standard playing card deck of 52 Card objects
class Deck:

	# Initializes a Deck object with different 52 Card objects
	def __init__(self):

		self.cardList = [] # the instance variable that represents the Deck as a list
		
		ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] # list of all ranks
		suits = ["C", "D", "H", "S"] # list of all suits

		for suit in suits:

			for rank in ranks:

				newCard = Card(rank,suit)
				self.cardList.append(newCard)


	# Shuffles the deck in a random order
	def shuffle(self):

		random.shuffle(self.cardList)

	# Deals the top Card of the Deck to a Player and adjusts the Player's hand and the Player's hand's point value
	# Parameter: player - the player that will be dealt the top Card from the Deck
	def dealOne(self, player):

		topCard = self.cardList.pop(0)
		player.hand.append(topCard)
		player.handTotal += topCard.value

	# Prints the entire Deck in four rows of 13 Cards
	# Return: a list of the entire Deck in four rows of 13 Cards
	def __str__(self):

		deckList = ""
		rowCount = 0
		
		for card in self.cardList:

			deckList += str(card)
			rowCount += 1

			if rowCount == 13: # continue printing but on the next row

				deckList += "\n"
				rowCount = 0
			else:

				deckList += "\t" 

		return deckList

# The Player class, which creates a player to play the game of Blackjack
class Player():

	# Initializes a Player object with a hand and a point value for the hand
	def __init__(self, name):

		self.name = name
		self.hand = [] # the instance variable for the Player's hand as a list
		self.handTotal = 0 # the instance variable for the Player's hand's point value

	# Updates the Player's hand's point value 
	def updateHandTotal(self):

		self.handTotal = 0
		for card in self.hand:

			self.handTotal += card.value

	# Returns the player's name 
	def getName(self):
		return self.name

	# Prints the Player's current hand when asked to print the Player object
	# Return: the Player's current hand in a list
	def __str__(self):

		handList = ""

		for card in self.hand:

			handList += str(card) + " "
		
		if handList == "": # if no cards in hand

			return "none"

		return handList

# Shows the face up hands of the Opponent and the Dealer
# Parameter: opponents - the list of Player objects that represents the opponents (the users)
# Parameter: dealer - the Player object that represents the dealer (the computer)
def showHands(opponents, dealer):

	print("\n")
	print("Dealer shows " + str(dealer.hand[1]) + " face up.") 	# Dealer's second card is face up
	
	for opponent in opponents:
		print(opponent.getName() + " shows " + str(opponent) + "face up.") 			# Player's cards are both faced up

# Goes through the game sequence for the opponent
# Parameter: cardDeck - the Deck of Cards that is used throughout the game
# Parameter: opponent - the Player object that represents the opponent (the user)
# Parameter: choice - the decision the Player object made to hit (1) or stay (2)
def opponentTurn(cardDeck, opponent, choice):

	print("\n")
	print(opponent.getName() + ", it's your turn.")
	print("\n")

	# choice = 1

	aceCount = 0 # counts how many aces the opponent has

	for index in range(0,len(opponent.hand)): # checking if an ace was dealt in the initial dealing

		if opponent.hand[index].rank == "A":
			
			aceCount += 1
			if aceCount == 1: 			# opponent dealt at least 1 ace initially
				
				opponent.hand[index].value = 11
				print("Assuming 11 points for an ace you were dealt for now.")

	opponent.updateHandTotal()

	if opponent.handTotal == 21: # if natural 21 / blackjack

		print("Natural 21!")
		return
	elif opponent.handTotal > 21: # if for some reason this function is run when the hand is already above 21, should return

		print(opponent.getName() + " your hand is greater than 21, you already bust!")
		return



	if choice == 1: # continues the game sequence while opponent wants to hit and the opponent's hand is less than 22; return breaks out of the loop

		print("You hold " + str(opponent) + "for a total of", opponent.handTotal)
		# choice = int(input("1 (hit) or 2 (stay)? "))

		cardDeck.dealOne(opponent)	# Deals the opponent the top Card from the Deck
		newCard = opponent.hand[len(opponent.hand) - 1] 	# the Card just dealt to the opponent
		print("\n")
		print("Card dealt: " + str(newCard))

		if newCard.rank == "A": 				# checks to see if new card dealt was an ace, and adjusts the value if needed
			
			aceCount += 1
			if aceCount == 1:
				
				opponent.hand[len(opponent.hand) - 1].value = 11
				opponent.updateHandTotal()
				
				if opponent.handTotal <= 21: 	# if don't bust from ace having a point value of 11, then make it an 11

					print("Assuming 11 points for the ace you were dealt for now.")
				else: 							# if would bust from making the ace have a point value of 11, then keep it as 1

					opponent.hand[len(opponent.hand) - 1].value = 1
					opponent.updateHandTotal()

		aceChange = False

		if aceCount > 0: # checks to see if some aces have not yet been changed from having a point value of 11 to 1					

			for card in opponent.hand:

				if card.rank == "A" and card.value == 11:

					aceChange = True

		if opponent.handTotal > 21 and aceChange:		# if about to bust, change all aces to have a point value of 1, if not already done so

			if aceCount > 0: 					

				print("Over 21. Switching an ace from 11 points to 1.")

				for card in opponent.hand:

					if card.rank == "A":

						card.value = 1

				opponent.updateHandTotal()

				print("New Total:", opponent.handTotal)
				print("\n")


		if opponent.handTotal > 21: 			# opponent busts even if all aces are changed to have a point value of 1

			print("You have " + str(opponent.handTotal) + ". You bust! You lose.", sep = "")
			print("\n")
			return

		if opponent.handTotal == 21:			# opponent gets a 21 so the game sequence moves on to the next player

			print("21! The next person should go now")
			return

	elif choice == 2:		# check to see if opponent chooses to stay / stand

		print("Staying with", opponent.handTotal)
		print("\n")
		return

# Goes through the game sequence for the dealer
# Parameter: cardDeck - the Deck of Cards that is used throughout the game
# Parameter: dealer - the Player object that represents the dealer (the computer)
# Parameter: opponents - the Player objects that represents the opponents (the users)
def dealerTurn(cardDeck, dealer, opponents):

	print("Dealer's turn")

	bustCounter = 0
	for opponent in opponents:

		if(opponent.handTotal > 21): 
			bustCounter += 1

	if bustCounter == len(opponents): # if all opponents busted, no need for dealer to play, so the game is over
		print("All opponents have busted! Dealer wins by default.")
		return

	for opponent in opponents:
		print(opponent.getName() + "'s hand: " + str(opponent) + "for a total of", opponent.handTotal)

	aceCount = 0 # counts how many aces the dealer has

	for index in range(0,len(dealer.hand)): # checking if an ace was dealt in the initial dealing

		if dealer.hand[index].rank == "A":
			aceCount += 1

			if aceCount == 1: 	# dealer dealt at least 1 ace initially
			
				dealer.hand[index].value = 11

	dealer.updateHandTotal()

	print("Dealer's hand: " + str(dealer) + "for a total of", dealer.handTotal) 		
	print("\n")
	
	if aceCount > 0: # dealer explains that the value of the ace has changed to 11 points
		print("Assuming 11 points for an ace I was dealt for now.")

	if dealer.handTotal == 21: # if dealer has natural 21 / blackjack, the dealer wins by default

		print("Natural 21! Dealer wins by default.")
		print("\n")
		return

	greaterPointCounter = 0
	for opponent in opponents:
		if dealer.handTotal >= opponent.handTotal: 

			greaterPointCounter += 1

	if greaterPointCounter == len(opponents): # if the dealer already has a hand greater than or equal to the opponents' hand, the dealer wins
		print("Dealer has " + str(dealer.handTotal) + ". Dealer wins!", sep = "")
		print("\n")
		return
	

	while True: # game continues until the dealer wins or busts; return breaks out of the loop

		cardDeck.dealOne(dealer)
		newCard = dealer.hand[len(dealer.hand) - 1]
		print("Dealer hits: " + str(newCard))
		print("New Total: ", dealer.handTotal)
		print("\n")

		if dealer.handTotal == 21:
			print("Dealer has 21! Dealer wins by default.")
			return

		if newCard.rank == "A": 					# checks to see if new card dealt was an ace, and adjusts the value if needed
			
			aceCount += 1
			if aceCount == 1:
				
				dealer.hand[len(dealer.hand) - 1].value = 11
				dealer.updateHandTotal()
				if dealer.handTotal <= 21: 		# if don't bust from ace having a point value of 11, then make it an 11

					print("Assuming 11 points for the ace you were dealt for now.")
				else: 							# if would bust from making the ace have a point value of 11, then keep it as 1

					dealer.hand[len(dealer.hand) - 1].value = 1
					dealer.updateHandTotal()

		aceChange = False

		if aceCount > 0: # checks to see if some aces have not yet been changed from having a point value of 11 to 1					

			for card in dealer.hand:

				if card.rank == "A" and card.value == 11:

					aceChange = True

		if dealer.handTotal > 21 and aceChange:		# if about to bust, change all aces to have a point value of 1, if not already done so

			if aceCount > 0: 					

				print("Over 21. Switching an ace from 11 points to 1.")

				for card in dealer.hand:

					if card.rank == "A":

						card.value = 1

				dealer.updateHandTotal()
				print("New Total:", dealer.handTotal)
				print("\n")

		if dealer.handTotal > 21: 			# dealer busts even if all aces are changed to have a point value of 1

			print("Dealer has " + str(dealer.handTotal) + ". Dealer busts!", sep = "")
			print("\n")
			return

		greaterPointCounter = 0
		for opponent in opponents:
			if dealer.handTotal >= opponent.handTotal: 

				greaterPointCounter += 1

		if  greaterPointCounter == len(opponents):	# dealer wins by default because the hand is worth the same or more than the opponents' hand

			print("Dealer has " + str(dealer.handTotal) + ". Dealer wins!", sep = "")
			print("\n")
			return

# The main program, which conducts the simplified game of Blackjack for the opponent and the dealer
def main():

	cardDeck = Deck()
	print("Initial Deck:")
	print(cardDeck)

	random.seed(50) 			# comment this line out to get a different outcome
	cardDeck.shuffle()
	print("Shuffled Deck:")
	print(cardDeck)

	dealer = Player("Dealer")
	opponent1 = Player("Player 1")
	opponent2 = Player("Player 2")

	cardDeck.dealOne(opponent1) 	# face up
	cardDeck.dealOne(opponent2) 	# face up
	cardDeck.dealOne(dealer) 		# the hole card, faced down
	cardDeck.dealOne(opponent1) 	# face up
	cardDeck.dealOne(opponent2) 	# face up
	cardDeck.dealOne(dealer) 		# face up

	print("Deck after dealing two cards each:")
	print(cardDeck)

	showHands([opponent1, opponent2], dealer)

	opponentTurn(cardDeck, dealer, opponent1)
	opponentTurn(cardDeck, dealer, opponent2)
	dealerTurn(cardDeck,dealer,[opponent1, opponent2])

	print ("Game over.")
	print ("Final hands:")
	print ("   Dealer:    " + str(dealer))
	print ("   Opponent:  " + str(opponent1))
	print ("   Opponent:  " + str(opponent2))


# main()