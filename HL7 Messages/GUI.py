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

        def hide_list(event):
            event.widget.pack_forget()

        # Multirequest patient list
        def Plist():
            if CheckVar1.get() == 1:
                Lb1 = Listbox(selectmode=SINGLE, height=5, yscrollcommand=1)
                Lb1.insert(1, "Winnie Franks")
                Lb1.insert(2, "Joan Roach")
                Lb1.insert(3, "Marie Evans")
                Lb1.insert(4, "Sally Jones")
                Lb1.insert(5, "John Foulkes")
                Lb1.insert(6, "Ian Potter")
                Lb1.insert(7, "Barry Birch")
                Lb1.insert(8, "Peter Parker")
                Lb1.insert(9, "Bill Sykes")
                Lb1.insert(10, "Mary Celeste")
                Lb1.place(x=40, y=100)
            elif CheckVar1.get() == 0:
                Lb1 = Listbox()
                Lb1.bind('<Button-1>', hide_list())
                Lb2 = Listbox(selectmode=SINGLE, height=1, yscrollcommand=0)
                Lb2.insert(1, "All")
                Lb2.place(x=40, y=100)



        def topten():
            print("Printed")
            #os.system("python topten.py")

        def cancel():
            print("Cancelled")

        def cdown():
            os.system("python C:\\Users\\lbroley\\PycharmProjects\\Sample360 Cleardowns\S360_Cleardown.py ")

        def close():
            root.destroy()

        # Buttons
        confirm = Button(root, text="Confirm", command=topten)
        cancel = Button(root, text="Cancel", command=cancel)
        cdown = Button(root, text="Clear database", command=cdown)
        close = Button(root, text="Close", command=close)

        confirm.place(x=169, y=570)
        cancel.place(x=229, y=570)
        cdown.place(x=282, y=570)
        close.place(x=377, y=570)

        # Entries
        L1 = Label(text="How many files would you like?:")
        L1.place(x=10, y=20)
        E1 = Entry(bd=2)
        E1.place(x=185, y=18)
        CheckVar1 = IntVar()
        C1 = Checkbutton(text="Muti request", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20, command=Plist)
        C1.place(x=-20, y=50)


root = Tk()
root.resizable(width=False, height=False)
root.geometry("600x600")
app = Window(root)

root.mainloop()
