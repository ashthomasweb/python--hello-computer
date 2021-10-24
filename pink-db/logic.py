
import ui
import dal_mysql
import dal_mongodb
import dal_test_db
import credentials

db = None
mydb = None

class DependencyInjection():

    global db

    def switch(input):
        global db
        global mydb

        if input == 1:
            # set active db to test module in DAL
            db = dal_test_db.test_db_1
            print('Interface connected to Test db1')
        elif input == 2:
            # get credentials and set active db to local MongoDB module in DAL
            dal_mongodb.myclient = credentials.myclient
            # connect module caller and global interface object
            db = dal_mongodb.GlobalCaller
            print('Interface connected to local MongoDB')
        elif input == 3:
            # get credentials and set active db to local MySQL module in DAL
            dal_mysql.mydb = credentials.db
            # set db server/query variable in DAL
            dal_mysql.set_db_server()
            # connect module caller and global interface object
            db = dal_mysql.GlobalCaller
            print('Interface connected to local MySQL')
        else: 
            print('failboat sailboat')
 

# db set by DI
# called from ui
# method run in appropriate DAL
class GlobalInterface():

    def show_all_db():
        db.show_all_db()

    def create_db():
        db.create_db()



    # # mock CRUD operations 
    # def create_test():
    #     db.create()

    # def read_test():
    #     db.read()

    # def update_test():
    #     db.update()

    # def delete_test():
    #     db.delete()


class Results():

    results = None

    def __init__(self):
        pass    

    def display_results(self):
        for x in self.results:
            ui.db_display_text.insert('1.0', f'{x}\n')

    def set_result(self, input):
        self.results = input
        self.display_results()


result_sender = Results()


# END of document
