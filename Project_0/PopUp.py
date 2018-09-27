from tkinter import *

def select():
    print ("You have selected " + variable.get())
    #master.quit()

def logIn():
    print("This section is to transport user to sign in section")

def addUser():
    print("This section is to add a User")


master = Tk()

variable = StringVar(master)
variable.set("(select person)") # default value

logIn = Button(master, text="Log In", command= logIn )
logIn.pack()

addUser = Button(master, text="Add User", command= addUser )
addUser.pack()

w = OptionMenu(master, variable, "Andrew", "Sujay", "Austin", "Brady", "Nikhil", "Hamza")
w.pack()

select = Button(master, text="Select", command= select )
select.pack()


mainloop()

