
import ui
import data
import credentials

db = None
mydb = None

class DependencyInjection():

    global db

    def switch(input):
        global db
        global mydb

        if input == 1:
            db = data.test_db_1
            print('db1')
        elif input == 2:
            db = data.test_db_2
            print('db2')
        elif input == 3:
            # data.mydb = credentials.db1
            db = data.test_db_3
            print('MySQL')
        else: 
            print('else')
 


class Interface():

    def create_ui():
        db.create()

    def read_ui():
        db.read()

    def update_ui():
        db.update()

    def delete_ui():
        db.delete()















