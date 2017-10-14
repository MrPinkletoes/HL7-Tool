#!/usr/bin/python
from tkinter import *

def topten ():
    print("Files Out")
def cancel():
    print("Cancelled")
def cdown():
    print("Database Cleared")
def close():
    root.destroy()


root = Tk()
root.title("HL7 Message Tool")
frame = Frame(root, bg="yellow", width="200", height="200")
frame.grid()

# Buttons
confirm = Button(root, text="Confirm", bg="green", fg="white", command=topten)
cancel = Button(root, text="Cancel", bg="red", fg="white", command=cancel)
cdown = Button(root, text= "Clear database", bg="blue", fg="white", command=cdown)
close = Button(root, text= "Close", bg="blue", fg="white", command=close)

cdown.grid(row=0, column=3)
confirm.grid(row=0)
cancel.grid(row=0, column=1)
close.grid(row=0, column=2)


root.mainloop()
