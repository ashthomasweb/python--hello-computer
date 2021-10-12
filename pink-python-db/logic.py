
import ui
import data


# 
# class Interface():
# DB = DependencyInjection()

# createFromUI():
    # DB.create

# readFromUI():
    # DB.read



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
 



def test():
    db.create()













