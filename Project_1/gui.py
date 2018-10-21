import tkinter as tk
import pandas as pd
from pandastable import Table, TableModel
from Budgetcode import *
 

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Budgeting Project')
        f = tk.Frame(self.main)
        f.pack()

        self.df = readInCSV('budget.csv')

        self.table = Table(f, dataframe=self.df,
                                showtoolbar=False, showstatusbar=False)
    
        self.table.show()

        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.modifyButton = tk.Button(self)
        self.modifyButton["text"] = "Modify Entry"
        self.modifyButton["command"] = self.modifyRowEntry
        self.modifyButton.pack(side="top")

        self.addButton = tk.Button(self)
        self.addButton["text"] = "Add New Expense"
        self.addButton["command"] = self.addNewExpense
        self.addButton.pack(side="top")

        self.deleteButton = tk.Button(self)
        self.deleteButton["text"] = "Delete Expense"
        self.deleteButton["command"] = self.say_hi
        self.deleteButton.pack(side="top")

        self.graphButton = tk.Button(self)
        self.graphButton["text"] = "Scatter Plot Graph"
        self.graphButton["command"] = timeseries
        self.graphButton.pack(side="top")

        self.graphButton = tk.Button(self)
        self.graphButton["text"] = "Pie Graph"
        self.graphButton["command"] = pie
        self.graphButton.pack(side="top")  

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        pass

    def addNewExpense(self):

        top = tk.Toplevel()
        top.title("Add New Expense")

        dateLabel = tk.Label(top, text='Date', font=('Times', 12))
        typeLabel = tk.Label(top, text='Category', font=('Times', 12))
        amountLabel = tk.Label(top, text='Amount', font=('Times', 12))

        dateLabel.grid(row=0,column=0)
        typeLabel.grid(row=1,column=0)
        amountLabel.grid(row=2,column=0)

        dateEntry = tk.Entry(top)
        typeEntry = tk.Entry(top)
        amountEntry = tk.Entry(top)

        dateEntry.grid(row=0,column=1)
        typeEntry.grid(row=1,column=1)
        amountEntry.grid(row=2,column=1)

        addButton = tk.Button(top,text="Add Expense",
                    command=lambda:[self.addExpenseToDf(dateEntry.get(),
                                    typeEntry.get(),
                                    amountEntry.get()),
                                    top.destroy()])

        addButton.grid(row=3,column=0)

    def addExpenseToDf(self, date, category, amount):
        self.df = newexpense(df=self.df, amount=amount, category=category, date=date)
        self.table.redraw()
        self.table.sortTable(0) # Sort by column index 0, which is date

    def modifyRowEntry(self):

        top = tk.Toplevel()
        top.title("Modify Row Entry")

        rowLabel = tk.Label(top, text='Row to Modify', font=('Times', 12))
        dateLabel = tk.Label(top, text='Date (Optional)', font=('Times', 12))
        typeLabel = tk.Label(top, text='Category (Optional)', font=('Times', 12))
        amountLabel = tk.Label(top, text='Amount (Optional)', font=('Times', 12))

        rowLabel.grid(row=0,column=0)
        dateLabel.grid(row=1,column=0)
        typeLabel.grid(row=2,column=0)
        amountLabel.grid(row=3,column=0)

        rowEntry = tk.Entry(top)
        dateEntry = tk.Entry(top)
        typeEntry = tk.Entry(top)
        amountEntry = tk.Entry(top)

        rowEntry.grid(row=0, column=1)
        dateEntry.grid(row=1,column=1)
        typeEntry.grid(row=2,column=1)
        amountEntry.grid(row=3,column=1)

        addButton = tk.Button(top,text="Modify Expense",
                    command=lambda:[self.modifyExpenseToDf(rowEntry.get(),
                                    dateEntry.get(),
                                    typeEntry.get(),
                                    amountEntry.get()),
                                    top.destroy()])

        addButton.grid(row=4,column=0)

    def modifyExpenseToDf(self, row, date, category, amount):
        try:
            row = int(row)
            row = row - 1 # Reduce row value by 1 to match with index value
        except: 
            print("Please enter an integer for the row value")
            return

        if row < 0 or row >= self.df.shape[0]:
            print("Please enter a valid integer value")
            return

        if date == "":
            date = None
        if category == "":
            category = None
        if amount == "":
            amount = None
        self.df = modifyEntry(df=self.df, row=row, date=date, category=category, amount=amount)
        self.table.redraw()
        self.table.sortTable(0) # Sort by column index 0, which is date


root = tk.Tk()
app = Application(master=root)

# To get around random crash with scroll pad
while True:
    try:
        app.update_idletasks()
        app.update()
    except UnicodeDecodeError:
        print("Caught Scroll Error")
    except tk.TclError:
        print("Closed App")
        break
