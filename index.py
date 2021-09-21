#!/usr/bin/python

import tkinter
import tkinter.messagebox
top = tkinter.Tk()
# Code to add widgets will go here...

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()

# END of document
