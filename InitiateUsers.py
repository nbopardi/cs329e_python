# Add Initial users

from Person import * 
import os
import pickle

userlist = []

hamza = Person(username='Hamza', description='sample description', image='1.png')
brady = Person(username='Brady', description='some deescp', image='3.png')
austin = Person(username='Austin', description='some deescp', image='4.png')
andrew = Person(username='Andrew', description='some deescp', image='Beedle.png')
sujay = Person(username='Sujay', description='some deescp', image='Phaser-Logo-Small.png')
nikhil = Person(username='Nikhil', description='some deescp', image='wallpaper-1366.jpg')

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