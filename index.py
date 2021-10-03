import mysql.connector

# import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import tkinter.messagebox
import tkinter.simpledialog


mydb = mysql.connector.connect(
  host="localhost",
  user="ashleyth",
  password="1473Pinkship!"
)


gui = tkinter.Tk()


# empty string for user's name
user = ''

# prompt user for their name
def hello_call_back():
   global user
   tkinter.messagebox.showinfo( 'Hello World!', 'Thanks for coming!')
   user = tkinter.simpledialog.askstring( 'Query:', "What's your name? Type Below:               " )
   name_call_back()

# disable hello method, prompt for entry, display in new frame
def name_call_back():
    # make available variable
    global user

    # disable initial "hello" button
    Begin['state'] = tkinter.DISABLED
    
    # create label for user entry
    enter_value=Label(greeting_frame, text= f"Hi {user}, I am Python. Please enter a value below:")
    enter_value.place(x=20, y=50)

    # create user entry field
    D = tkinter.Entry(greeting_frame, width= 40 )
    D.place(x=20, y=70)

    # create text field
    display_input=Text(response_frame)

    # empty string for user input
    user_input = ''
   
    # gets user entered value and sends it to response frame
    def input_driver():
        user_input = D.get()
        make_new_frame(user_input)

    # builds response frame and inserts user entered value
    def make_new_frame(input):
        response_frame.place(x= 20, y= 230)   
        display_input.insert('1.0', f'{user}, you entered: {input}\n')
        display_input.pack()
    
    # displays entered string in response_frame
    E = tkinter.Button(greeting_frame, text ='Ok', command = input_driver)
    E.place(x=20, y=90)

# layout frames
hello_frame = ttk.Frame(gui, width= 340, height= 460)
hello_frame['relief'] = 'raised'
hello_frame.place(x= 230, y= 20)
hello_frame.pack_propagate(False)

greeting_frame = ttk.Frame(hello_frame, width= 300, height= 200)
greeting_frame['relief'] = 'sunken'
greeting_frame.place(x= 20, y= 20)
greeting_frame.pack_propagate(False)

response_frame = ttk.Frame(hello_frame, width= 300, height= 200)
response_frame['relief'] = 'groove'
response_frame.pack_propagate(False)

# Initial 'Hello" button and beginning of name input callback chain
Begin = tkinter.Button(greeting_frame, text ='Hello', command = hello_call_back)
Begin.place(x=20, y=10)



# Database Operations

s = Style()
s.configure('My.TFrame', background='pink')

db_frame = ttk.Frame(gui, width= 500, height= 300, style='My.TFrame')
db_frame['relief'] = 'raised'
db_frame.place(x= 150, y= 500)
db_frame.config()
db_frame.pack_propagate(False)

# create label for user entry
section_title=Label(db_frame, text= "Create A Database")
section_title.place(x=10, y=10)

# create label for user entry
enter_title=Label(db_frame, text= "Enter name below:")
enter_title.place(x=10, y=35)

# create user entry field
F = tkinter.Entry(db_frame, width= 40 )
F.place(x=10, y=60)


mycursor = mydb.cursor()
# gets user entered value
temp_db_name = ""
def create_db_driver():
    temp_db_name = F.get()
    mycursor.execute(f"CREATE DATABASE {temp_db_name}")


G = tkinter.Button(db_frame, text ='Create', command = create_db_driver)
G.place(x=260, y=56)





# new_frame = ttk.Frame(a, width= 10, height= 15)
# new_frame['relief'] = 'groove'
# new_frame.place(x= 2, y= 5)





# Calculator


# main window styling options
gui.title('Hello, Meta... Python Desktop Application')
gui.geometry('800x900')

# run program
gui.mainloop()

# END of document
