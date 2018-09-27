# Add Initial users

from Person import * 
import os
import pickle

userlist = []

hamzaDesc = 'My name is Hamza and I love UT football, python and running!'
bradyDesc = 'My name is Brady and I love gaming, music, and napping.'
austinDesc = 'Hey, I am Austin. I like Frisbee, LoL, and Korean.'
andrewDesc = 'My name is Andrew and I love gaming, and basketball.'
sujayDesc = 'My name is Sujay and I love sports and food!'
nikhilDesc = 'My name is Nikhil and I like python.'

hamza = Person(username='Hamza', description=hamzaDesc, image='IMG_4475.jpg')
brady = Person(username='Brady', description=bradyDesc, image='IMG_4472.jpg')
austin = Person(username='Austin', description=austinDesc, image='IMG_4478.jpg')
andrew = Person(username='Andrew', description=andrewDesc, image='IMG_4477.jpg')
sujay = Person(username='Sujay', description=sujayDesc, image='IMG_4476.jpg')
nikhil = Person(username='Nikhil', description=nikhilDesc, image='nikhil_profile.png')

userlist.append(hamza)
userlist.append(brady)
userlist.append(austin)
userlist.append(andrew)
userlist.append(sujay)
userlist.append(nikhil)


# for i in userlist:
# 	print (i.getImage())

with open('userlist.pkl', 'wb') as f:
	pickle.dump(userlist, f)
