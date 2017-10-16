#!/usr/bin/python
import os
from tkinter import *
from HL7_Message_Creation import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # changing the title of our master widget
        self.master.title("HL7 Tool")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=0)

        def topten():
            print("Printed")
            #os.system("python topten.py")

        def cancel():
            print("Cancelled")

        def cdown():
            os.system("python S360_Cleardown.py ")

        def close():
            root.destroy()

        # Buttons
        confirm = Button(root, text="Confirm", command=topten)
        cancel = Button(root, text="Cancel", command=cancel)
        cdown = Button(root, text="Clear database", command=cdown)
        close = Button(root, text="Close", command=close)

        cdown.place(x=163, y=570)
        confirm.place(x=50, y=570)
        cancel.place(x=110, y=570)
        close.place(x=258, y=570)


root = Tk()
root.resizable(width=False, height=False)
root.geometry("600x600")
app = Window(root)

root.mainloop()
