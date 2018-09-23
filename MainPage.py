from tkinter import *
from Person import * 
from PIL import Image, ImageTk
import os


userlist = [Person("Hamza", description='some desc'),Person("Austin")]

logflag = False

currentuser = None

def start():
    main = Tk()
    main.geometry("200x200")
    main.title(maintitle())

    variable = StringVar(main)
    variable.set("(select person)")
    a = OptionMenu(main,variable,*returnUsersNames(userlist))
    a.grid(row=0,column=0)

    
 

    logIn = Button(main, text=logbuttontext(), command= lambda: [quit(main), logbuttoncommand()])
    # logIn.place(x = 20, y = 30 )
    logIn.grid(row=1,column=0)

    addUser = Button(main, text="Add User", command= lambda: [quit(main), add()])
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
    
    f = Label(adding,text = "Description:")
    f.grid(row=1,column = 0)
    g = Entry(adding)
    g.grid(row = 1, column = 1)


    imageBrowser = ImageBrowser(adding)

    e = Button(adding,text="Add",command= lambda: [addtoList(name=d.get(), description=g.get(), photo=imageBrowser.getPhoto()),quit(adding),start()])
    e.grid(row=3,column=0)

# def browseImage(member):

#     from tkinter import filedialog

#     Tk().withdraw() 
#     filename = filedialog.askopenfilename()
#     print(filename)

#     photo = ImageTk.PhotoImage(Image.open(filename))
#     member.setImage(photo)

#     print (member.getUsername())
#     print (member.getDescription())
#     print (member.getImage())

def maintitle():
    global currentuser
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
        logout()

def errorcheck(username, page):
    quit(page)
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

def logout():
    global logflag
    global currentuser
    logflag = False
    currentuser = None
    start()

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

    logUser = Button(logPage, text = "Log In", command= lambda: [errorcheck(userLogIn.get(), logPage)])
    logUser.grid(row=2, column=1)

    logPage.mainloop()

def quit(m):
    m.destroy()

def addtoList(name, description, photo):
    newUser = Person(username=name, description=description, image=photo)

    print( newUser.getUsername())
    print ( newUser.getDescription())
    print (newUser.getImage())
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

        # somephoto = ImageTk.PhotoImage(Image.open("Beedle.png"))

        userPhotoLocation = user.getImage()
        img = Image.open(userPhotoLocation)
        img = img.resize((250,250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)

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

from shutil import copy
class ImageBrowser:

    def __init__(self, master):

        imageBrowser = Button(master, text="Browse Image", command=self.browseImage)
        imageBrowser.grid(row=2, column=0)

        self.photoLocation = None # will be path name of where photo is located

    def browseImage(self):

        from tkinter import filedialog

        Tk().withdraw() 
        filepath = filedialog.askopenfilename()
        # print(filepath)

        # self.assignImage(filename) 

        imageDir = os.getcwd() + '/images/'

        if not os.path.exists(imageDir):
            os.makedirs(imageDir)

        path, filename = os.path.split(filepath)
        
        endpath = copy(filepath, imageDir)

        self.photo = endpath

    def getPhoto(self):

        return self.photo






def main():
    start()





main()
