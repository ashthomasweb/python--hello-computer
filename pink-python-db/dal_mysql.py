import mysql.connector

import logic
import ui


current_db = ""

# MySQL database queries - needs interface

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
    
def recheck_db():
    global mycursor
    # global cursor object created empty at runtime
    mycursor = mydb.cursor()


# gets user entered value
user_text_entry = ""


# create
def create_db_driver():
    user_text_entry = ui.F.get()
    mycursor.execute(f"CREATE DATABASE {user_text_entry}")

# read
def show_all_db():
    recheck_db()
    mycursor.execute("SHOW DATABASES")
    ui.db_display_text.delete('1.0', 'end')
    for x in mycursor:
        ui.db_display_text.insert('1.0', f'{x}\n')


def show_tables():
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
            ui.db_display_text.insert('1.0', f'{x}\n')


# command
def sql_command():
    user_text_entry = ui.F.get()
    mycursor.execute(f"{user_text_entry}")
    for x in mycursor:
            ui.db_display_text.insert('1.0', f'{x}\n')

# test/development
def display_cursor():
    for x in mycursor:
            ui.db_display_text.insert('1.0', f'{x}\n')

    ui.db_display_text.insert('1.0', f'{mydb}\n')




def connect_to_db():
    global current_db
    current_db = ui.F.get()
    def_db()
    ui.db_display_text.delete('1.0', 'end')
    ui.db_display_text.insert('1.0', f'{mydb}\n')
    

# TEST INTERFACE


class test_db_1():
    def create():
        print('test1: create')

    def read():
        print('test1: read')

    def update():
        print('test1: update')

    def delete():
        print('test1: delete')



class test_db_2():
    def create():
        print('test2: create')

    def read():
        print('test2: read')

    def update():
        print('test2: update')

    def delete():
        print('test2: delete')



class test_db_3():
    def create():
        print('test3: create')

    def read():
        print('test3: read')

    def update():
        print('test3: update')

    def delete():
        print('test3: delete')