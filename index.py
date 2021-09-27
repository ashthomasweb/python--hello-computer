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
   name_call_back()


def name_call_back():
    global user
    name_hello=Label(greeting_frame, text= f"Hi {user}, I'm Python. Please enter a value below:")
    name_hello.place(x=20, y=50)
    D = tkinter.Entry(greeting_frame, width= 40 )
    D.place(x=20, y=70)
    response_frame = ttk.Frame(gui, width= 300, height= 200)
    display_input=Text(response_frame)
    user_input = ""

    def take_input(entry_input):
        print(entry_input.get())
        user_input = entry_input.get()
        print(user_input)
    
    print(user_input)

    def input_driver():
        take_input(D)
        make_new_frame(user_input)

    def make_new_frame(input):
        print(input)

        response_frame['relief'] = 'sunken'
        response_frame.place(x= 20, y= 250)   
        display_input.insert('1.0', f'{user}, you entered: {input}')
        display_input.pack()
        
    E = tkinter.Button(greeting_frame, text ='Ok', command = input_driver)
    E.place(x=20, y=90)
       
# user_input not passing correctly - WIP



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
