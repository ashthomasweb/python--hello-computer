
# import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.messagebox
import tkinter.simpledialog
import logic
import dal_mysql as data

gui = tkinter.Tk()
btn = tkinter.Button

# frame and styling
s = ttk.Style()
s.configure('My.TFrame', background='pink')
s.configure('Bar.TFrame', background='light blue')

db_select_frame = ttk.Frame(gui, width= 900, height= 40, style='Bar.TFrame')
db_select_frame.place(x= 0, y= 0)

db_frame = ttk.Frame(gui, width= 900, height= 660, style='My.TFrame')
db_frame['relief'] = 'raised'
db_frame.place(x= 0, y= 40)
db_frame.config() # What does this do?
db_frame.pack_propagate(False)

server_oper_frame = ttk.Frame(db_frame, width= 500, height= 60)
server_oper_frame['relief'] = 'groove'
server_oper_frame.place(x= 10, y= 10)

entry_frame = ttk.Frame(db_frame, width= 500, height= 60)
entry_frame['relief'] = 'groove'
entry_frame.place(x= 10, y= 80)

db_oper_frame = ttk.Frame(db_frame, width= 370, height= 130)
db_oper_frame['relief'] = 'groove'
db_oper_frame.place(x= 520, y= 10)


# text display area
db_display_frame = ttk.Frame(db_frame, width= 880, height= 490)
db_display_frame['relief'] = 'groove'
db_display_frame.place(x= 10, y= 160)
db_display_frame.pack_propagate(False)

# create text field
db_display_text=Text(db_display_frame)
db_display_text.pack(expand=True)
# db_display.place(x= 50, y= 100)

# title for section
server_title=Label(server_oper_frame, text= "Server Operations")
server_title.place(x=5, y=1)

db_oper_title=Label(db_oper_frame, text= "Database Operations")
db_oper_title.place(x= 5, y=1)

# label for user entry
enter_title=Label(entry_frame, text= "Enter a value or command below:")
enter_title.place(x= 5, y=1)

# user entry field
F = tkinter.Entry(entry_frame, width= 66 )
F.place(x=10, y=30)



# buttons

# Global Operations
G = btn(server_oper_frame, text ='Create DB', command = logic.GlobalInterface.create_db)
G.place(x= 10, y= 25)

L = btn(server_oper_frame, text ='View All DB', command = logic.GlobalInterface.show_all_db)
L.place(x= 80, y= 25)

I = btn(server_oper_frame, text ='Connect to:', command = data.connect_to_db)
I.place(x=160, y= 25)

J = btn(entry_frame, text ='Run\nCommand', height =2, width = 8, command = data.sql_command)
J.place(x=425, y=10)

# Database Operations
K = btn(db_oper_frame, text ='Show Tables', command = data.show_tables)
K.place(x=10, y=25)

# DI Switch - Database selection
N = btn(db_select_frame, text ='DI Test DB', width = 12, command = lambda: logic.DependencyInjection.switch(1))
N.place(x=200, y=10)

O = btn(db_select_frame, text ='Local MongoDB', width = 12, command = lambda: logic.DependencyInjection.switch(2))
O.place(x=300, y=10)

P = btn(db_select_frame, text ='Local MySQL', width = 12, command = lambda: logic.DependencyInjection.switch(3))
P.place(x=400, y=10)



# # TEST CRUD
# M = btn(db_frame, text ='Interface Create', command = logic.GlobalInterface.create_test)
# M.place(x=100, y=162)

# Q = btn(db_frame, text ='Interface Read', command = logic.GlobalInterface.read_test)
# Q.place(x=200, y=162)

# R = btn(db_frame, text ='Interface Update', command = logic.GlobalInterface.update_test)
# R.place(x=300, y=162)

# S = btn(db_frame, text ='Interface Delete', command = logic.GlobalInterface.delete_test)
# S.place(x=400, y=162)
# # TEST CRUD





# main window styling options

gui.title('Pink DB')
gui.geometry('900x700')

# END of document
