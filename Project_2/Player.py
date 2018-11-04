# select number of players
# cycle through players
# vote on which answer choice is the best
# select winner and award point value
# give winner the chance to answer multiple choice question for bonus points
# first to 10 points wins (2 for caption, 1 for mc)

# Player class

class Player():

	def __init__(self, name):

		self.playerName = name
		self.pointValue = 0

	def addPoints(self, pointsEarned):

		self.pointValue = self.pointValue + pointsEarned

		if self.pointValue < 0:
			self.pointValue = 0

	def getPointValue(self):

		return self.pointValue

	def getName(self):
		
		return self.playerName
