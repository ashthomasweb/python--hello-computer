import mysql.connector

# import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import tkinter.messagebox
import tkinter.simpledialog

gui = tkinter.Tk()

# frame and styling
s = Style()
s.configure('My.TFrame', background='pink')
db_frame = ttk.Frame(gui, width= 820, height= 620, style='My.TFrame')
db_frame['relief'] = 'raised'
db_frame.place(x= 40, y= 40)
db_frame.config()
db_frame.pack_propagate(False)

# text display area
db_display_frame = ttk.Frame(db_frame, width= 800, height= 450)
db_display_frame['relief'] = 'groove'
db_display_frame.place(x= 10, y= 160)
db_display_frame.pack_propagate(False)

# create text field
db_display_text=Text(db_display_frame)
db_display_text.pack(expand=True)
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

# global cursor object created empty at runtime
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
    for x in mycursor:
            db_display_text.insert('1.0', f'{x}\n')

    db_display_text.insert('1.0', f'{mydb}\n')

# buttons
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

# main window styling options
gui.title('PinkPy DB')
gui.geometry('900x700')

# run program
gui.mainloop()
