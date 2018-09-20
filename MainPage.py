from tkinter import *
from Person import * 
from PIL import Image, ImageTk

userlist = [Person("Hamza", description='some desc'),Person("Austin")]

def start():
    main = Tk()
    main.geometry("200x200")

    variable = StringVar(main)
    variable.set("(select person)")
    a = OptionMenu(main,variable,*returnUsersNames(userlist))
    a.grid(row=0,column=0)

    
 

    logIn = Button(main, text="Log In", command=login )
    # logIn.place(x = 20, y = 30 )
    logIn.grid(row=1,column=0)

    addUser = Button(main, text="Add User", command= add )
    # addUser.place(x = 80, y = 30)
    addUser.grid(row=0,column=1)




    
    b = Button(main,text="Select",command= lambda: [viewUserProfile(getPersonByUsername(variable.get())),quit(main)])
    b.grid(row=2,column=0)
    
    exitbutton = Button(main,text="Quit",command= lambda: [quit(main)])
    exitbutton.grid(row = 2, column = 1)

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
    e.grid(row=2,column=0)
    f = Label(adding,text = "Description:")
    f.grid(row=1,column = 0)
    g = Entry(adding)
    g.grid(row = 1, column = 1)
    exitbutton = Button(adding,text="Quit",command= lambda: [quit(main)])
    exitbutton.grid(row = 2, column = 1)

def login():
    pass

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

def viewUserProfile(user):

    viewing = Tk()
    viewing.geometry("200x200")

    NameLabel = Label(viewing,text=user.getUsername())
    NameLabel.grid(row=0,column=0)

    DescriptionLabel = Label(viewing,text=user.getDescription())
    DescriptionLabel.grid(row=1,column=0)

    back = Button(viewing,text="Back",command= lambda: [quit(viewing),start()])
    back.grid(row=2,column=0)

def main():
    start()





main()
