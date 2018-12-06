# settings.py

from tkinter import Text, END

def init(master):
    global console
    console = Text(master, width = 100)
    console.configure(state="disabled")

def write(message):

	console.configure(state="normal")
	console.insert(END, message)
	console.see(END)
	console.configure(state="disabled")
