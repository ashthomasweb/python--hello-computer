import mysql.connector

# import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import tkinter.messagebox
import tkinter.simpledialog





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
    enter_value=Label(greeting_frame, text= f"Hi {user}, I am Python. Please enter a value:")
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
        response_frame.place(x= 310, y= 20)   
        display_input.insert('1.0', f'{user}, you entered: {input}\n')
        display_input.pack()
    
    # displays entered string in response_frame
    E = tkinter.Button(greeting_frame, text ='Ok', command = input_driver)
    E.place(x=20, y=90)

# layout frames
hello_frame = ttk.Frame(gui, width= 640, height= 260)
hello_frame['relief'] = 'raised'
hello_frame.place(x= 65, y= 20)
hello_frame.pack_propagate(False)

greeting_frame = ttk.Frame(hello_frame, width= 270, height= 200)
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

# frame and styling
s = Style()
s.configure('My.TFrame', background='pink')
db_frame = ttk.Frame(gui, width= 500, height= 600, style='My.TFrame')
db_frame['relief'] = 'raised'
db_frame.place(x= 150, y= 380)
db_frame.config()
db_frame.pack_propagate(False)

## CREATE database

# text display area
db_display_frame = ttk.Frame(db_frame, width= 480, height= 390)
db_display_frame['relief'] = 'groove'
db_display_frame.place(x= 10, y= 190)
db_display_frame.pack_propagate(False)
# create text field
db_display_text=Text(db_display_frame)
db_display_text.pack(expand=False)
# db_display.place(x= 50, y= 100)


# title for section
section_title=Label(db_frame, text= "Create A Database")
section_title.place(x=10, y=10)

# label for user entry
enter_title=Label(db_frame, text= "Enter name below:")
enter_title.place(x=10, y=35)

# user entry field
F = tkinter.Entry(db_frame, width= 40 )
F.place(x=10, y=60)


# MySQL database queries - needs interface
current_db = ""

mydb = mysql.connector.connect(
  host="localhost",
  user="ashleyth",
  password="1473Pinkship!",
  database=f"{current_db}"
)

def def_db():
    global mydb
    global mycursor
    mydb = mysql.connector.connect(
      host="localhost",
      user="ashleyth",
      password="1473Pinkship!",
      database=f"{current_db}"
    )
    mycursor = mydb.cursor()




    

mycursor = mydb.cursor()
# gets user entered value
user_text_entry = ""

def create_db_driver():
    user_text_entry = F.get()
    mycursor.execute(f"CREATE DATABASE {user_text_entry}")

def view_all_db():
    mycursor.execute("SHOW DATABASES")
    db_display_text.delete('1.0', 'end')
    for x in mycursor:
        db_display_text.insert('1.0', f'{x}\n')

def connect_to_db():
    global current_db
    current_db = F.get()
    def_db()

    # mydb = mysql.connector.connect(
    #     host="localhost",
    #     user="ashleyth",
    #     password="1473Pinkship!",
    #     database=f"{user_text_entry}"
    # )
    # mycursor = mydb.cursor()
    
    db_display_text.delete('1.0', 'end')
    db_display_text.insert('1.0', f'{mydb}\n')
    
def sql_command():
    user_text_entry = F.get()
    mycursor.execute(f"{user_text_entry}")
    for x in mycursor:
            db_display_text.insert('1.0', f'{x}\n')

def show_tables():
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
            db_display_text.insert('1.0', f'{x}\n')

def display_cursor():
    # for x in mycursor:
    #         db_display_text.insert('1.0', f'{x}\n')
    
    db_display_text.insert('1.0', f'{mydb}\n')




G = tkinter.Button(db_frame, text ='Create', command = create_db_driver)
G.place(x=260, y=56)

H = tkinter.Button(db_frame, text ='View All', command = view_all_db)
H.place(x=310, y=56)

I = tkinter.Button(db_frame, text ='Connect to:', command = connect_to_db)
I.place(x=380, y=56)

J = tkinter.Button(db_frame, text ='SQL Command:', command = sql_command)
J.place(x=400, y=26)

K = tkinter.Button(db_frame, text ='Show Tables', command = show_tables)
K.place(x=300, y=26)

L = tkinter.Button(db_frame, text ='Cursor Contents', command = display_cursor)
L.place(x=200, y=26)

# new_frame = ttk.Frame(a, width= 10, height= 15)
# new_frame['relief'] = 'groove'
# new_frame.place(x= 2, y= 5)





# Calculator


# main window styling options
gui.title('Hello, Meta... Python Desktop Application')
gui.geometry('800x1000')

# run program
gui.mainloop()

# END of document
