import tkinter as tk
import pandas as pd
from pandastable import Table, TableModel
 

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Budgeting Project')
        f = tk.Frame(self.main)
        f.pack()

        df = pd.read_csv('budget.csv')

        self.table = Table(f, dataframe=df,
                                showtoolbar=False, showstatusbar=False)
    
        self.table.show()

        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.modifyButton = tk.Button(self)
        self.modifyButton["text"] = "Modify Entry"
        self.modifyButton["command"] = self.say_hi
        self.modifyButton.pack(side="top")

        self.addButton = tk.Button(self)
        self.addButton["text"] = "Add New Expense"
        self.addButton["command"] = self.say_hi
        self.addButton.pack(side="top")

        self.deleteButton = tk.Button(self)
        self.deleteButton["text"] = "Delete Expense"
        self.deleteButton["command"] = self.say_hi
        self.deleteButton.pack(side="top")

        self.graphButton = tk.Button(self)
        self.graphButton["text"] = "Scatter Plot Graph"
        self.graphButton["command"] = self.say_hi
        self.graphButton.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
# app.mainloop()

while True:
    try:
        app.update_idletasks()
        app.update()
    except UnicodeDecodeError:
        print("Caught Scroll Error")
    except tk.TclError:
        print("Closed App")
        break