
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
            print('test db1')
        elif input == 2:
            db = dal_mongodb.GlobalCaller
            print('Connected to MongoDB local')
        elif input == 3:
            dal_mysql.mydb = credentials.db1_server
            # needs to choose 
            db = dal_mysql.GlobalCaller
            print('Conntected to MySQL local')
        else: 
            print('failboat sailboat')
 


class GlobalInterface():

    def show_all_db_ui():
        db.show_all_db()

    def create_db_ui():
        db.create_db()




    def create_test():
        db.create()

    def read_test():
        db.read()

    def update_test():
        db.update()

    def delete_test():
        db.delete()



# Not working...

class Results():

    results = None

    def __init__(self):
        pass    

    def send_results(results):
        print(results)
        # for x in results:
        #     ui.db_display_text.insert('1.0', f'{x}\n')


result_sender = Results()






    












