
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
gui.geometry('1200x800')

# COMMAND SECTIONS

# DB Selection
# frame
db_select_frame = ttk.Frame(gui, width= 1200, height= 40, style='Bar.TFrame')
db_select_frame.place(x= 0, y= 0)

# test commands
T = btn(db_select_frame, text ='Test Command', width = 12, command = logic.test_method)
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
operations_frame = ttk.Frame(gui, width= 1200, height= 760, style='My.TFrame')
operations_frame['relief'] = 'raised'
operations_frame.place(x= 0, y= 40)
operations_frame.config() # What does this do?
operations_frame.pack_propagate(False)

# Server operations (server-level CRUD)
# frame
server_oper_frame = ttk.Frame(operations_frame, width= 550, height= 95)
server_oper_frame['relief'] = 'groove'
server_oper_frame.place(x= 10, y= 10)
server_op_title=Label(server_oper_frame, text= "Server Operations")
server_op_title.place(x=5, y=1)

# Global Operations Interface
G = btn(server_oper_frame, text ='Create DB', command = logic.GlobalInterface.create_db)
G.place(x= 10, y= 25)

L = btn(server_oper_frame, text ='View All DB', command = logic.GlobalInterface.show_all_db)
L.place(x= 80, y= 25)

M = btn(server_oper_frame, text ='Drop DB', command = logic.GlobalInterface.delete_db)
M.place(x= 165, y= 25)

I = btn(server_oper_frame, text ='Connect to:', command = logic.GlobalInterface.connect_to_db)
I.place(x=10, y= 60)


# Database operations (intra-database CRUD)
# frame
db_oper_frame = ttk.Frame(operations_frame, width= 550, height= 95)
db_oper_frame['relief'] = 'groove'
db_oper_frame.place(x= 10, y= 115)
db_oper_title=Label(db_oper_frame, text= "Database Operations")
db_oper_title.place(x= 5, y=1)

# operations buttons
J = btn(db_oper_frame, text ='Create Table', height =1, width = 11, command = logic.DatabaseInterface.create_table)
J.place(x=10, y=25)

K = btn(db_oper_frame, text ='All Tables', width= 11, command = logic.DatabaseInterface.show_all_tables)
K.place(x=190, y=25)

Q = btn(db_oper_frame, text ='Rename Table To:', command = logic.DatabaseInterface.rename_table)
Q.place(x= 10, y= 60)

update_table_to = tkinter.Entry(db_oper_frame)
update_table_to.place(x= 114, y= 60, width= 155, height = 26)

R = btn(db_oper_frame, text ='Delete Table', width= 11, command = logic.DatabaseInterface.delete_table)
R.place(x= 100, y= 25)

S = btn(db_oper_frame, text ='View Table', width= 11, command = logic.DatabaseInterface.view_table)
S.place(x= 280, y= 25)

T = btn(db_oper_frame, text ='View Columns', command = logic.DatabaseInterface.view_columns)
T.place(x= 370, y= 25)

U = btn(db_oper_frame, text ='Cross Ref:', command = logic.DatabaseInterface.cross_columns)
U.place(x= 277, y= 60)

cross_col1 = tkinter.Entry(db_oper_frame)
cross_col1.place(x= 340, y= 60, width= 100, height = 26)

cross_col2 = tkinter.Entry(db_oper_frame)
cross_col2.place(x= 440, y= 60, width= 100, height = 26)


# DISPLAY SECTIONS

# Command area parent frame
command_frame = ttk.Frame(operations_frame, width= 550, height= 490)
command_frame['relief'] = 'groove'
command_frame.place(x= 10, y= 220)
command_frame.pack_propagate(False)

# User Input
# frame
entry_frame = ttk.Frame(command_frame, width= 546, height= 478)
entry_frame.place(x= 1, y= 1)
enter_title=Label(command_frame, text= "Enter a value or command below:")
enter_title.place(x= 10, y=3)

# command field
command_text=Text(command_frame)
command_text.place(x=10, y=25, width= 530, height= 420)


# run command button
J = btn(command_frame, text ='Run Command', height =1, width = 12, command = logic.GlobalInterface.run_command)
J.place(x=445, y=455)


# Query area parent frame
query_frame = ttk.Frame(operations_frame, width= 620, height= 490)
query_frame['relief'] = 'groove'
query_frame.place(x= 570, y= 220)
query_frame.pack_propagate(False)

# Connection info display frame
connection_display_frame = ttk.Frame(query_frame, width= 600, height= 52)
connection_display_frame['relief'] = 'groove'
connection_display_frame.place(x= 10, y= 10)
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
message_wrapper_frame = ttk.Frame(operations_frame, width= 620, height= 200)
message_wrapper_frame['relief'] = 'groove'
message_wrapper_frame.place(x= 570, y= 10)
message_wrapper_frame.pack_propagate(False)

message_display_frame = ttk.Frame(message_wrapper_frame, width= 600, height= 165)
message_display_frame['relief'] = 'groove'
message_display_frame.place(x= 10, y= 25)
message_display_frame.pack_propagate(False)
message_display_text=Text(message_display_frame, wrap=WORD)
message_display_text.pack(expand=True)
messages_title=Label(message_wrapper_frame, text= "System messages:")
messages_title.place(x= 8, y=3)

# Query display frame and text
db_query_frame = ttk.Frame(query_frame, width= 600, height= 389)
db_query_frame['relief'] = 'groove'
db_query_frame.place(x= 10, y= 90)
db_query_frame.pack_propagate(False)
db_query_text=Text(db_query_frame, wrap=WORD)
db_query_text.pack(expand=True)
query_title=Label(query_frame, text= "Your Query:")
query_title.place(x= 8, y=70)



# END of document
