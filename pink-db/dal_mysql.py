# import mysql.connector

import logic
import ui

# current_db = ""

# global database and cursor variables created empty at runtime
mydb = None # set by DependencyInjection

myserver = None # set by DAL GlobalCaller
myquery = None # set by DAL GlobalCaller
user_text_entry = ""

current_db = ""

class GlobalCaller():

    def show_all_db():
        # set_db_server()
        myserver.execute("SHOW DATABASES")
        ui.db_display_text.delete('1.0', 'end')
        logic.result_sender.set_result(myserver)

    # create
    def create_db():
        user_text_entry = ui.F.get()
        myserver.execute(f"CREATE DATABASE {user_text_entry}")


def set_db_server():
    global myserver
    global myquery
    global mydb

    # global cursor object created empty at runtime
    myserver = mydb.server.cursor()
    
    myquery = mydb.query.cursor()



def show_tables():

    myquery.execute("SHOW TABLES")

    for x in myquery:
            ui.db_display_text.insert('1.0', f'{x}\n')


def sql_command():
    user_text_entry = ui.F.get()
    myserver.execute(f"{user_text_entry}")
    for x in myserver:
            ui.db_display_text.insert('1.0', f'{x}\n')


def connect_to_db():
    global current_db
    current_db = ui.F.get()
    
    # set_db_server()

    ui.db_display_text.delete('1.0', 'end')
    ui.db_display_text.insert('1.0', f'{mydb}\n')
    set_db_server()
    



def test_method():
    print(mydb.current_db)
    print(mydb.query)
    





# test/development
# def display_cursor():
#     for x in mycursor:
#             ui.db_display_text.insert('1.0', f'{x}\n')

#     ui.db_display_text.insert('1.0', f'{mydb}\n')

# END of document
