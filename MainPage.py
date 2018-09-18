from tkinter import *
from Person import * 

userlist = [Person("Hamza"),Person("Austin")]

def start():
    main = Tk()
    main.geometry("200x200")

    variable = StringVar(main)
    variable.set("(select person)")
    a = OptionMenu(main,variable,*returnUsersNames(userlist))
    a.grid(row=0,column=0)


    b = Button(main,text="Add",command= lambda: [add(),quit(main)])
    b.grid(row=1,column=0)

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

def quit(m):
    m.destroy()

def addtoList(name):
    newUser = Person(name)
    userlist.append(newUser)
    print(userlist)


def main():
    start()





main()