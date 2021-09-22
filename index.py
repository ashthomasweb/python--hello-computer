#!/usr/bin/python

# import tkinter
from tkinter import *

import tkinter.messagebox
import tkinter.simpledialog


# from tkinter import *
# from tkinter import ttk

gui = tkinter.Tk()
# Code to add widgets will go here...

user = ""

def helloCallBack():
   global user
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")
#    hello.pack()
#    hello=Label(gui, text= f"Hi {user}, I'm Python. Please enter a value below:")
   
   C = tkinter.simpledialog.askstring( "Question", "What's your name? Type Below" )
   user = C
   print(C)
   fireName()

def fireName():
   nameCallBack()
   


def nameCallBack():
    global user
    nameHello=Label(gui, text= f"Hi {user}, I'm Python. Please enter a value below:")
    nameHello.pack()
    D = tkinter.Entry(gui, width= 80 )
    # printValue(D) # WIP
    D.pack()


# def printValue(arg):
#     print(arg)



B = tkinter.Button(gui, text ="Hello", command = helloCallBack)

B.pack()

gui.geometry("800x600")
gui.mainloop()

# END of document
