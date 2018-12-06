import tkinter as tk
from Blackjack import *
import settings
from PIL import Image, ImageTk


class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	# Sets up the buttons for the game suite
	def create_widgets(self):

		self.playBlackJack = tk.Button(self)
		self.playBlackJack["text"] = "Click to play Blackjack"
		self.playBlackJack["command"] = self.createGame
		self.playBlackJack.pack(side="top")

		#self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
		#self.quit.pack(side="bottom")


	def createGame(self):
		# Set up the game
		cardDeck = Deck()

		# random.seed(50) 			# comment this line out to get a different outcome
		
		cardDeck.shuffle()

		dealer = Player("Dealer")
		p1 = Player("Player 1")
		p2 = Player("Player 2")

		cardDeck.dealOne(p1) 			# face up
		cardDeck.dealOne(p2) 			# face up
		cardDeck.dealOne(dealer) 		# the hole card, faced down
		cardDeck.dealOne(p1) 			# face up
		cardDeck.dealOne(p2) 			# face up
		cardDeck.dealOne(dealer) 		# face up

		# Create the window for the game
		top = tk.Toplevel()
		top.geometry("1000x1000")

		# Create text output for the game
		settings.init(top)
		settings.console.grid(row=35,columnspan=5)
		settings.write("Welcome to Blackjack!")

		# Contains all the cards for player 1
		p1CardLabels = []

		p1CardLabels.append(tk.Label(top))
		p1CardLabels.append(tk.Label(top))

		# Update graphics for player 1's starting cards
		self.updateImages(p1, p1CardLabels, top, row=0)

		# Contains all the cards for player 2
		p2CardLabels = []

		p2CardLabels.append(tk.Label(top))
		p2CardLabels.append(tk.Label(top))

		# Update graphics for player 2's starting cards
		self.updateImages(p2, p2CardLabels, top, row=5)

		# Contains all the cards for the dealer
		dealerCardLabels = []

		dealerCardLabels.append(tk.Label(top))
		dealerCardLabels.append(tk.Label(top))

		# Update graphics for dealer's starting cards (doesn't reveal 'hole' card)
		self.updateImagesDealer(dealer, dealerCardLabels, row=10, column=0)

		# Button for 'hit' for player 1
		p1Hit = tk.Button(top, text='Player 1 Hit', command=lambda:[self.hit(p1, p1CardLabels, top, cardDeck)])
		p1Hit.grid(row=0,column=5)

		# Button for 'stay' for player 1
		p1Stay = tk.Button(top, text='Player 1 Stay', command=lambda:	[self.stay(p1, cardDeck),
																		p1Hit.configure(state="disabled"),
																		p1Stay.configure(state="disabled")])
		p1Stay.grid(row=0,column=6)
		
		# Button for 'hit' for player 2
		p2Hit = tk.Button(top, text='Player 2 Hit', command=lambda:[self.hit(p2, p2CardLabels, top, cardDeck)])
		p2Hit.grid(row=5,column=5)

		# Button for 'stay' for player 2
		p2Stay = tk.Button(top, text='Player 2 Stay', command=lambda:	[self.stay(p2, cardDeck),
																		p2Hit.configure(state="disabled"),
																		p2Stay.configure(state="disabled")])
		p2Stay.grid(row=5,column=6)

		dealersTurn = tk.Button(top, text="Dealer's Turn", command=lambda:	[p1Hit.configure(state="disabled"),
																			p1Stay.configure(state="disabled"),
																			p2Hit.configure(state="disabled"),
																			p2Stay.configure(state="disabled"),
																			dealerTurn(cardDeck, dealer, [p1,p2]), 
																			self.updateImages(dealer, dealerCardLabels, top, row=10),
																			dealersTurn.configure(state="disabled"),
																			self.gameOver(dealer, p1, p2)])
		dealersTurn.grid(row=10, column=5)


	# Request a new card from the deck to be added to a player's hand
	def hit(self, player, labels, parent, cardDeck):

		opponentTurn(cardDeck, player, choice=1) # 1 = hit
		labels.append(tk.Label(parent))

		row = 0
		if player.getName() == "Player 2": # if player 2 is hitting, then the row for grid is 5 rather than 0
			row = 5
		
		self.updateImages(player, labels, parent, row=row)

	# Player stays with his or her current hand
	def stay(self, player, cardDeck):

		opponentTurn(cardDeck, player, choice=2) # 2 = stay

	# Updates the graphics for the player's hand
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
			# labels[i].grid(row=row,column=i)
			labels[i].grid(row=row,columnspan=i+1)


	# Function for dealer's inital hand to prevent the 'hold' card from being displayed
	def updateImagesDealer(self, dealer, labels, row, column):

		cards = str(dealer).split()

		# Graphics for 'hole' card
		hiddenImageName = 'cards/back.gif'
		hiddenImage = Image.open(hiddenImageName)
		hiddenPhoto = ImageTk.PhotoImage(hiddenImage)
		
		labels[0].configure(image=hiddenPhoto)
		labels[0].image = hiddenPhoto
		labels[0].grid(row=row, column=column)

		# Graphics for shown card
		imageName = 'cards/' + cards[1].lower() + '.gif'
		image = Image.open(imageName)
		photo = ImageTk.PhotoImage(image)

		labels[1].configure(image=photo)
		labels[1].image = photo
		labels[1].grid(row=row,columnspan=column+2)

	# Considers the end game totals to determine who wins
	def gameOver(self, dealer, p1, p2):

		settings.write("\nGame over.")
		settings.write("\nFinal hands:")
		settings.write("\n   Dealer:    " + str(dealer))
		settings.write("\n   Player 1:  " + str(p1))
		settings.write("\n   Player 2:  " + str(p2))
		settings.write("\n")
		if dealer.handTotal == 21:
			settings.write("Dealer wins!")

		elif dealer.handTotal < 21:

			if p1.handTotal > dealer.handTotal and p1.handTotal <= 21:
				if (p2.handTotal < 21 and p1.handTotal > p2.handTotal) or p2.handTotal > 21: 
					settings.write(p1.getName() + " wins!")


			if p2.handTotal > dealer.handTotal and p2.handTotal <= 21:
				if (p1.handTotal < 21 and p2.handTotal > p1.handTotal) or p1.handTotal > 21:
					settings.write(p2.getName() + " wins!")

			if p1.handTotal == p2.handTotal:
				if (p1.handTotal > 21 and p2.handTotal > 21):
					settings.write("Dealer wins, players lose.")
				else:
					settings.write("It's a tie between ", p1.getName() + " and " + p2.getName() + ".")

		else:

			if (p1.handTotal > p2.handTotal and p1.handTotal <= 21) or (p1.handTotal <= 21 and p2.handTotal > 21):
				settings.write(p1.getName() + " wins!")

			if (p2.handTotal > p1.handTotal and p2.handTotal <= 21) or (p2.handTotal <= 21 and p1.handTotal > 21):
				settings.write(p2.getName() + " wins!")

			if p1.handTotal == p2.handTotal and p1.handTotal <= 21 and p2.handTotal <= 21:
				settings.write("It's a tie between ", p1.getName() + " and " + p2.getName() + ".")			

#def main():
        #root = tk.Tk()
        #app = Application(master=root)
        #app.mainloop()
#main()
