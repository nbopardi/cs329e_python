# select number of players
# cycle through players
# vote on which answer choice is the best
# select winner and award point value
# give winner the chance to answer multiple choice question for bonus points
# first to 10 points wins (2 for caption, 1 for mc)

# Player class

class Player():

	def __init__(self, name, isJudge=False, caption = ''):

		self.playerName = name
		self.pointValue = 0
		self.isJudge = isJudge
		self.caption = caption

	# Add (or subtract) points to the player's total
	def addPoints(self, pointsEarned):

		self.pointValue = self.pointValue + pointsEarned

		if self.pointValue < 0:
			self.pointValue = 0

	# Gets the player's point value
	def getPointValue(self):
		return self.pointValue

	# Gets the player's name
	def getName(self):
		return self.playerName

	# Set if the player is the judge or not for the round (True or False)
	def setJudge(self, isJudgeForRound):
		self.isJudge = isJudgeForRound

	# Store the user's latest answer for the "Caption-this" mode
	def storeAnswer(self, answer):
		self.caption = answer

	# Retreive the user's latest answer
	def getAnswer(self):
		return self.caption
