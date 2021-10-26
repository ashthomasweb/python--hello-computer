import logic
import ui
from traceback import format_exc

# global database and cursor variables created empty at runtime
mydb = None # set by DependencyInjection
myserver = None # set by DAL GlobalCaller


entry = lambda: logic.entry_getter.get_entry()

# called from logic layer
def set_db_server():
    global myserver
    global mydb
    # global cursor object created empty at runtime
    myserver = mydb.server.cursor()
    

class GlobalCaller():

    # create
    def create_db():
        try:
            myserver.execute(f"CREATE DATABASE {entry()}")
            myserver.execute("SHOW DATABASES")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"Succesful creation of new database: {entry()}")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

    # read
    def show_all_db():
        try:
            myserver.execute("SHOW DATABASES")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"All databases on server:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

    # update

    # delete

    # make db connection
    def connect_to_db():
        try:
            myserver.execute(f"USE {entry()}")
            myserver.execute("SHOW TABLES")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"Connected to database: {entry()}\nAll contents (if any) displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

        display_current_db()

    # run language-specific command
    def run_command():
        try:
            myserver.execute(f"{entry()}")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"Results (if any) of custom command displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

        display_current_db()




class DatabaseCaller():

    # read
    def show_tables():
        try:
            myserver.execute("SHOW TABLES")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"All tables displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))







# Helper function
def display_current_db():
    myserver.execute('SELECT DATABASE()')
    logic.result_sender.set_database_info(myserver)
    # for x in myserver:
    #     ui.db_display_text.insert('1.0', f'{x}\n')







# END of document
