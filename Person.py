# Person.py
# Defines the class for a generic Person in Project 0
import os
class Person():

	# Requires a username
	# Profile image and user description are optional
	def __init__(self, username, image=None, description=''):

		self.setUsername(username)
		self.setImage(image)
		self.setDescription(description)

	# Gets the username
	def getUsername(self):
		return self.username

	# Sets the username
	def setUsername(self, newName):
		self.username = newName

	# Gets the profile image
	def getImage(self):
		return (os.getcwd() + '/images/' + self.profImage) # returns a path to the profile image

	# Sets the profile image
	def setImage(self, newImage):
		self.profImage = newImage

	# Gets the description
	def getDescription(self):
		return self.description

	# Sets the description
	def setDescription(self, newDesc):
		self.description = newDesc


