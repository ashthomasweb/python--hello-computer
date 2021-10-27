
import ui
import dal_mysql
import dal_mongodb
import dal_test_db
import credentials
from traceback import format_exc

serv_op = None
db_op = None
mydb = None

class DependencyInjection():

    global serv_op
    global db_op


    def switch(input):
        global serv_op
        global db_op
        global mydb

        if input == 1:
            # set active db to test module in DAL
            serv_op = dal_test_db.test_db_1
            # set connection info display
            result_sender.set_server_info('Test DB')
        elif input == 2:
            # get credentials and set active db to local MongoDB module in DAL
            dal_mongodb.myclient = credentials.myclient
            # connect global and database caller to interface
            serv_op = dal_mongodb.GlobalCaller
            db_op = dal_mongodb.DatabaseCaller
            # set connection info display
            result_sender.set_server_info('MongoDB Local')
        elif input == 3:
            # get credentials and set active db to local MySQL module in DAL
            dal_mysql.mydb = credentials.db
            # set db server/query variable in DAL
            dal_mysql.set_db_server()
            # connect global and database caller to interface
            serv_op = dal_mysql.GlobalCaller
            db_op = dal_mysql.DatabaseCaller
            # set connection info display
            result_sender.set_server_info('MySQL Local')
        else: 
            # need error handling and messaging
            print('failboat sailboat')
 

# db set by DI
# called from ui
# method run in appropriate DAL
class GlobalInterface():

    def show_all_db():
        serv_op.show_all_db()

    def create_db():
        serv_op.create_db()

    def delete_db():
        serv_op.delete_db()

    def connect_to_db():
        serv_op.connect_to_db()

    def run_command():
        serv_op.run_command()




class DatabaseInterface():

    def create_table():
        db_op.create_table()
    
    def show_all_tables():
        db_op.show_all_tables()

    def rename_table():
        db_op.rename_table()

    def delete_table():
        db_op.delete_table()

    def view_table():
        db_op.view_table()

    def view_columns():
        db_op.view_col_names()

    def cross_columns():
        db_op.cross_columns()
    



# WORKER CLASSES



# Sends query results
class Results():

    results = None
    server = None
    database = None

    def __init__(self):
        pass    

    def display_results(self):
        
        ui.db_query_text.delete('1.0', 'end')
        for x in self.results:
            ui.db_query_text.insert('1.0', f'{x}\n')

    def set_result(self, input):
        self.results = input
        self.display_results()

    def display_server(self):
        ui.server_display_text.delete('1.0', 'end')
        ui.server_display_text.insert('1.0', f'{self.server}\n')
        print(f'Interface connected to {self.server}')

    def set_server_info(self, input):
        self.server = input
        self.display_server()

    def display_database(self):
        ui.db_display_text.delete('1.0', 'end')
        for x in self.database:
            ui.db_display_text.insert('1.0', f'{x}')
        str = ui.db_display_text.get('1.0', 'end')
        disallowed_characters = "(),"
        for character in disallowed_characters:
            str = str.replace(character, "")
        ui.db_display_text.delete('1.0', 'end')
        ui.db_display_text.insert('1.0', f'{str}')
            
    def set_database_info(self, input):
        self.database = input
        self.display_database()

    # unclear seperation of concerns...
    def get_database_name(self):
        return ui.db_display_text.get('1.0', 'end-1c')


# Displays system messages and error reporting
class Messages():

    message = ''
    
    def __init__(self):
        pass

    def display_message(self):
        ui.message_display_text.delete('1.0', 'end')
        ui.message_display_text.insert('1.0', f'{self.message}')
        
    def set_message(self, input):
         self.message = input
         self.display_message()


# Returns user input from text field
class UserEntry():

    entry = None
    cross1 = None
    cross2 = None

    def __init__(self):
        pass

    def get_entry(self):
        self.entry = ui.command_text.get('1.0','end')
        return self.entry

    def get_entry_trunc(self):
        self.entry = ui.command_text.get('1.0','end-1c')
        return self.entry

    def get_update_table(self):
        self.entry = ui.update_table_to.get()
        return self.entry

    def get_cross1(self):
        self.cross1 = ui.cross_col1.get()
        return self.cross1
    
    def get_cross2(self):
        self.cross2 = ui.cross_col2.get()
        return self.cross2
    


# WORKER OBJECTS
result_sender = Results()
message_sender = Messages()
entry_getter = UserEntry()



# Development functions - not for usage in program architecture
def test_method():
    # print(ui.command_text.get('1.0', 'end'))
    print(type(result_sender.results))
    # print(ui.update_table_to.get())





# END of document
