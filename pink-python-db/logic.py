
import ui
import data


db = None

class DependencyInjection():
# switch to pick db
# if: user select
# then: get selected db
# DB = user select
    global db

    def switch(input):
        global db
        if input == 1:

            db = data.test_db_1
            print('db1')
            db.create()
        elif input == 2:
            db = data.test_db_2
            print('db2')
        elif input == 3:
            db = data.test_db_3
            print('db3')
        else: 
            print('hell0')
 


class Interface():

    def create_ui():
        db.create()

    def read_ui():
        db.read()

    def update_ui():
        db.update()

    def delete_ui():
        db.delete()















