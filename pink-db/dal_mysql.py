import logic
from traceback import format_exc

# global database and cursor variables created empty at runtime
mydb = None # set by DependencyInjection
myserver = None # set by DAL GlobalCaller


entry = lambda: logic.entry_getter.get_entry()
entry_trunc = lambda: logic.entry_getter.get_entry_trunc()
get_update_table = lambda: logic.entry_getter.get_update_table()
db_name = lambda: logic.result_sender.get_database_name()
cross_1 = lambda: logic.entry_getter.get_cross1()
cross_2 = lambda: logic.entry_getter.get_cross2()


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
    def delete_db():
        try:
            myserver.execute(f"DROP DATABASE {entry()}")
            myserver.execute("SHOW DATABASES")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"Succesfully dropped database: {entry()}")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

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

    def create_table():
        try:
            myserver.execute(f"CREATE TABLE {entry()} (id INT)")
            myserver.execute("SHOW TABLES")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"Empty table '{entry_trunc()}' created:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

    # read
    def show_all_tables():
        try:
            myserver.execute("SHOW TABLES")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"All tables displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

    def view_table():
        try:
            myserver.execute(f"SELECT * FROM {entry()}")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"All table data displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

    def view_col_names():
        try:
            myserver.execute(f"SELECT COLUMN_NAME  FROM INFORMATION_SCHEMA.COLUMNS  WHERE TABLE_SCHEMA = {db_name()} AND TABLE_NAME = '{entry_trunc()}'")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"All columns in {entry_trunc()} displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

    def cross_columns():
        try:
            myserver.execute(f"SELECT {cross_1()}, {cross_2()} FROM {entry_trunc()}")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"Reference {cross_1()} by {cross_2()} below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))


    # update 
    def rename_table():
        try:
            myserver.execute(f"RENAME TABLE {entry()} TO {get_update_table()}")
            myserver.execute("SHOW TABLES")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"Table name successfully updated. All tables displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

    # delete
    def delete_table():
        try:
            myserver.execute(f"DROP TABLE {entry()}")
            myserver.execute("SHOW TABLES")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"Table successfully deleted. All tables displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))


# Helper function
def display_current_db():
    myserver.execute('SELECT DATABASE()')
    logic.result_sender.set_database_info(myserver)
  


# END of document
