from tkinter import *
from Person import * 

userlist = [Person("Hamza"),Person("Austin")]

logflag = False

currentuser = None

def start():
    main = Tk()
    main.geometry("200x200")
    main.title(maintitle)

    variable = StringVar(main)
    variable.set("(select person)")
    a = OptionMenu(main,variable,*returnUsersNames(userlist))
    a.grid(row=0,column=0)
 

    logIn = Button(main, text= logbuttontext(), command= logbuttoncommand)
    # logIn.place(x = 20, y = 30 )
    logIn.grid(row=1,column=0)

    addUser = Button(main, text="Add User", command= add )
    # addUser.place(x = 80, y = 30)
    addUser.grid(row=2,column=0)




    
    b = Button(main,text="Select",command= lambda: [viewUserProfile(getPersonByUsername(variable.get())),quit(main)])
    b.grid(row=3,column=0)

    # profileButton = Button(main,text="View Profile",command= lambda: [viewUserProfile(getPersonByUsername(variable.get())),quit(main)])
    # profileButton.grid(row=4,column=0)


    mainloop()

#this function returns a list of names of users to be displayed on the main
def returnUsersNames(objectList):
    people =[]
    for x in objectList:
        people.append(x.getUsername())
    return people

def add():

    adding = Tk()
    adding.geometry("200x200")

    c = Label(adding,text="Name:")
    c.grid(row=0,column=0)
    d = Entry(adding)
    d.grid(row=0,column=1)
    e = Button(adding,text="Add",command= lambda: [addtoList(d.get()),quit(adding),start()])
    e.grid(row=1,column=0)

def maintitle():
    global currentuser
    print (currentuser)
    print (currentuser.getUsername())
    if (currentuser == None):
        return "Guest"
    else:
        return currentuser.getUsername()

def swaplogflag():
    global logflag
    if (logflag == False):
        logflag = True
    else:
        logflag = False

def logbuttontext():
    global logflag
    if (logflag == True):
        return "Log Out"
    else:
        return "Log In"

def logbuttoncommand():
    global logflag
    if (logflag == False):
        login("Log In")
    else:
        logflag = False
        start()

def errorcheck(username):
    global currentuser
    for i in userlist:
        current = i.getUsername()
        if (current == username):
            currentuser = i
            swaplogflag()
            start()
    login("Error")

def checkname(name):
    check = Tk()
    check.title(name)
    
def login(title):
    logPage = Tk()
    logPage.title(title)
    logPage.geometry("225x100")

    caption = Label(logPage, text = "Username")
    caption.grid(row=1, column=0)

    back = Button(logPage, text = "Back", command=lambda:[logPage.destroy(), start()])
    back.grid(row=0, column=2)
    
    userLogIn = Entry(logPage)
    userLogIn.grid(row=1, column=1)

    logUser = Button(logPage, text = "Log In", command= lambda: [errorcheck(userLogIn.get()), quit(logPage)])
    logUser.grid(row=2, column=1)

    logPage.mainloop()

def quit(m):
    m.destroy()

def addtoList(name):
    newUser = Person(name)
    userlist.append(newUser)
    print(userlist)

def getPersonByUsername(username):

    for individual in userlist:
        if username == individual.getUsername():
            return individual

    return None

def viewUserProfile(somePerson):

    profile = Tk()
    profile.geometry("200x200")

    print(somePerson.getUsername())

def main():
    start()





main()
