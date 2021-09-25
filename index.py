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
    nameHello=Label(greeting_frame, text= f"Hi {user}, I'm Python. Please enter a value below:")
    nameHello.place(x=20, y=50)
    D = tkinter.Entry(greeting_frame, width= 40 )
    D.place(x=20, y=70)
    response_frame = ttk.Frame(gui, width= 300, height= 200)

    def takeInput(entryInput):
        print(entryInput.get())
        userInput = entryInput.get()
        displayInput=Text(response_frame)

    def inputDriver():
        takeInput(D)
        makeNewFrame()

    def makeNewFrame():
        response_frame['relief'] = 'sunken'
        response_frame.place(x= 20, y= 250)   
        displayInput.insert('1.0', f'{user}, you entered: {userInput}')
        displayInput.pack()
        
    E = tkinter.Button(greeting_frame, text ='Ok', command = inputDriver)
    E.place(x=20, y=90)
       




greeting_frame = ttk.Frame(gui, width= 300, height= 200)
greeting_frame['relief'] = 'sunken'
greeting_frame.place(x= 20, y= 50)
greeting_frame.pack_propagate(False)

# Initial 'Hello" button and beginning of name input callback chain
B = tkinter.Button(greeting_frame, text ='Hello', command = hello_call_back)
B.place(x=20, y=10)





gui.title('Hello, Meta... Python Desktop Application')
gui.geometry('800x600')
gui.mainloop()

# END of document
