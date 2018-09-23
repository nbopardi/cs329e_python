from tkinter import *
from Person import * 
from PIL import Image, ImageTk
import os

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
    addUser.grid(row=2,column=0)




    
    b = Button(main,text="Select",command= lambda: [viewUserProfile(getPersonByUsername(variable.get()), main)])
    # b = Button(main,text="Select",command= lambda: [topLevel])

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
    e.grid(row=2,column=0)
    f = Label(adding,text = "Description:")
    f.grid(row=1,column = 0)
    g = Entry(adding)
    g.grid(row = 1, column = 1)

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

def viewUserProfile(user, master):

    profile = Profile(master, user, title="User Profile")

    

class Profile(Toplevel):

    def __init__(self, parent, user, title = None):

        self.profile = Toplevel() 

        if title:
            self.profile.title(title)

        self.parent = parent

        body = Frame(self.profile)
        self.initial_focus = self.body(body, user)
        body.pack(padx=5, pady=5)

        self.buttonbox()

        self.profile.grab_set() # makes sure that no mouse or keyboard events are sent to the wrong window

        if not self.initial_focus:
            self.initial_focus = self

        self.profile.protocol("WM_DELETE_WINDOW", self.cancel)

        self.initial_focus.focus_set() # need to explicitly move the keyboard focus to the dialog

        self.profile.wait_window()

    #
    # construction hooks

    def body(self, master, user):
        # create dialog body.  return widget that should have
        # initial focus. 
        username = user.getUsername()
        description = user.getDescription()
        Label(master, text=username).grid(row=0)
        Label(master, text=description).grid(row=1)

        photo = ImageTk.PhotoImage(Image.open("Beedle.png"))
        # photo = user.getImage()
        imageLabel = Label(master, image=photo)
        imageLabel.grid(row=2, column=0)
        imageLabel.image = photo

        return imageLabel # return the initial focus


    def buttonbox(self):
        # add standard button box

        box = Frame(self.profile)

        w = Button(box, text="Back", width=10, command=self.cancel, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)

        self.profile.bind("<Escape>", self.cancel)

        box.pack()


    def cancel(self, event=None):

        # put focus back to the parent window
        self.parent.focus_set()

        self.profile.destroy()




def main():
    start()





main()
