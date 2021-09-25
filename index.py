#!/usr/bin/python

# import tkinter
from tkinter import *
from tkinter import ttk

import tkinter.messagebox
import tkinter.simpledialog

gui = tkinter.Tk()

# empty string for user's name
user = ''


def hello_call_back():
   global user
   tkinter.messagebox.showinfo( 'Hello World!', 'Thanks for coming!')
   user = tkinter.simpledialog.askstring( 'Question', "What's your name? Type Below:" )
   print(user)
   nameCallBack()


def nameCallBack():
    global user
    nameHello=Label(gui, text= f"Hi {user}, I'm Python. Please enter a value below:")
    nameHello.pack()
    D = tkinter.Entry(gui, width= 40 )
    D.pack()

    def takeInput(entryInput):
       print(entryInput.get())
       userInput = entryInput.get()
       displayInput=Text(response_frame)
       displayInput.pack()
       displayInput.insert('1.0', f'{user}, you entered: {userInput}')

    def inputDriver():
       takeInput(D)
       makeNewFrame()

    def makeNewFrame():
       response_frame = ttk.Frame(gui, width= 300, height= 200)
       response_frame['relief'] = 'sunken'
       response_frame.place(x= 20, y= 250)   



    E = tkinter.Button(response_frame, text ='Ok', command = inputDriver)
    E.pack()
       




greeting_frame = ttk.Frame(gui, width= 300, height= 200)
greeting_frame['relief'] = 'sunken'
greeting_frame.place(x= 20, y= 50)

# Initial 'Hello" button and beginning of name input callback chain
B = tkinter.Button(greeting_frame, text ='Hello', command = hello_call_back)
B.place(x=20, y=10)





gui.title('Hello, Meta... Python Desktop Application')
gui.geometry('800x600')
gui.mainloop()

# END of document
