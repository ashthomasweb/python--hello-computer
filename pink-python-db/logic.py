
import ui
import dal_mysql
import dal_mongodb
import credentials

db = None
mydb = None

class DependencyInjection():

    global db

    def switch(input):
        global db
        global mydb

        if input == 1:
            db = dal_mysql.test_db_1
            print('db1')
        elif input == 2:
            db = dal_mongodb.myclient
            print('db2')
        elif input == 3:
            dal_mysql.mydb = credentials.db1_server
            # needs to choose 
            db = dal_mysql.mydb
            print('MySQL')
        else: 
            print('else')
 


class Interface():

    def show_all_db_ui():
        db.show_all_db()

    def create_ui():
        db.create()

    def read_ui():
        db.read()

    def update_ui():
        db.update()

    def delete_ui():
        db.delete()















