
# import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.messagebox
import tkinter.simpledialog

# import software layers
import logic
import dal_mysql as data

# UI common object variable assignment
gui = tkinter.Tk()
btn = tkinter.Button

# frame styling
s = ttk.Style()
s.configure('My.TFrame', background='pink')
s.configure('Bar.TFrame', background='light blue')

# main window styling options
gui.title('Pink DB')
gui.geometry('900x720')

# COMMAND SECTIONS

# DB Selection
# frame
db_select_frame = ttk.Frame(gui, width= 900, height= 40, style='Bar.TFrame')
db_select_frame.place(x= 0, y= 0)

# test commands
T = btn(db_select_frame, text ='Test Command', width = 12, command = data.test_method)
T.place(x=10, y=10)

# DI Switch - selection buttons
N = btn(db_select_frame, text ='DI Test DB', width = 12, command = lambda: logic.DependencyInjection.switch(1))
N.place(x=200, y=10)

O = btn(db_select_frame, text ='Local MongoDB', width = 12, command = lambda: logic.DependencyInjection.switch(2))
O.place(x=300, y=10)

P = btn(db_select_frame, text ='Local MySQL', width = 12, command = lambda: logic.DependencyInjection.switch(3))
P.place(x=400, y=10)

# Primary Operations
# frame
operations_frame = ttk.Frame(gui, width= 900, height= 680, style='My.TFrame')
operations_frame['relief'] = 'raised'
operations_frame.place(x= 0, y= 40)
operations_frame.config() # What does this do?
operations_frame.pack_propagate(False)

# Server operations (server-level CRUD)
# frame
server_oper_frame = ttk.Frame(operations_frame, width= 500, height= 60)
server_oper_frame['relief'] = 'groove'
server_oper_frame.place(x= 10, y= 10)
server_op_title=Label(server_oper_frame, text= "Server Operations")
server_op_title.place(x=5, y=1)

# Global Operations Interface
G = btn(server_oper_frame, text ='Create DB', command = logic.GlobalInterface.create_db)
G.place(x= 10, y= 25)

L = btn(server_oper_frame, text ='View All DB', command = logic.GlobalInterface.show_all_db)
L.place(x= 80, y= 25)

I = btn(server_oper_frame, text ='Connect to:', command = data.connect_to_db)
I.place(x=160, y= 25)







# User Input
# frame
entry_frame = ttk.Frame(operations_frame, width= 500, height= 60)
entry_frame['relief'] = 'groove'
entry_frame.place(x= 10, y= 80)
enter_title=Label(entry_frame, text= "Enter a value or command below:")
enter_title.place(x= 5, y=1)

# entry field
F = tkinter.Entry(entry_frame, width= 66 )
F.place(x=10, y=30)

# run command button
J = btn(entry_frame, text ='Run\nCommand', height =2, width = 8, command = data.sql_command)
J.place(x=425, y=10)



# Database operations (intra-database CRUD)
# frame
db_oper_frame = ttk.Frame(operations_frame, width= 370, height= 130)
db_oper_frame['relief'] = 'groove'
db_oper_frame.place(x= 520, y= 10)
db_oper_title=Label(db_oper_frame, text= "Database Operations")
db_oper_title.place(x= 5, y=1)

# operations buttons
K = btn(db_oper_frame, text ='Show Tables', command = data.show_tables)
K.place(x=10, y=25)

# DISPLAY SECTIONS
# Display area parent frame
display_frame = ttk.Frame(operations_frame, width= 880, height= 510)
display_frame['relief'] = 'groove'
display_frame.place(x= 10, y= 160)
display_frame.pack_propagate(False)

# Connection info display frame
connection_display_frame = ttk.Frame(display_frame, width= 600, height= 52)
connection_display_frame['relief'] = 'groove'
connection_display_frame.place(x= 120, y= 10)
connection_display_frame.pack_propagate(False)

# server
server_display_frame = ttk.Frame(connection_display_frame, width= 200, height= 20)
server_display_frame['relief'] = 'groove'
server_display_frame.place(x= 10, y= 23)
server_display_frame.pack_propagate(False)
server_display_text=Text(server_display_frame)
server_display_text.pack(expand=True)
server_title=Label(connection_display_frame, text= "Server Connection")
server_title.place(x= 8, y=3)

# database
db_display_frame = ttk.Frame(connection_display_frame, width= 370, height= 20)
db_display_frame['relief'] = 'groove'
db_display_frame.place(x= 220, y= 23)
db_display_frame.pack_propagate(False)
db_display_text=Text(db_display_frame)
db_display_text.pack(expand=True)
db_title=Label(connection_display_frame, text= "Database")
db_title.place(x= 218, y=3)

# Message/Log display frame
message_display_frame = ttk.Frame(display_frame, width= 600, height= 40)
message_display_frame['relief'] = 'groove'
message_display_frame.place(x= 120, y= 85)
message_display_frame.pack_propagate(False)
message_display_text=Text(message_display_frame)
message_display_text.pack(expand=True)
messages_title=Label(display_frame, text= "Messages:")
messages_title.place(x= 120, y=65)

# Query display frame and text
db_query_frame = ttk.Frame(display_frame, width= 600, height= 350)
db_query_frame['relief'] = 'groove'
db_query_frame.place(x= 120, y= 150)
db_query_frame.pack_propagate(False)
db_query_text=Text(db_query_frame)
db_query_text.pack(expand=True)
query_title=Label(display_frame, text= "Your Query:")
query_title.place(x= 118, y=130)



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




# END of document
