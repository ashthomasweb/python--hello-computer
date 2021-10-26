import logic
import ui

# global database and cursor variables created empty at runtime
mydb = None # set by DependencyInjection
myserver = None # set by DAL GlobalCaller


entry = lambda: logic.entry_getter.get_entry()

def set_db_server():
    global myserver
    global mydb
    # global cursor object created empty at runtime
    myserver = mydb.server.cursor()
    

class GlobalCaller():

    def show_all_db():
        # set_db_server()
        try:
            myserver.execute("SHOW DATABASES")
            logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"All databases on server:")

        except BaseException as err:
            logic.message_sender.set_message(f"{err}")


    # create
    def create_db():
        myserver.execute(f"CREATE DATABASE {entry()}")

    # delete





# STILL NEEDS INTERFACE! 
def show_tables():

    myserver.execute("SHOW TABLES")

    for x in myserver:
        ui.db_query_text.insert('1.0', f'{x}\n')


def sql_command():
    myserver.execute(f"{entry()}")
    for x in myserver:
        ui.db_query_text.insert('1.0', f'{x}\n')
            
    display_current_db()

def connect_to_db():
    try:
        myserver.execute(f"USE {entry()}")
        logic.message_sender.set_message(f"Connected to database: {entry()}")
    except BaseException as err:
        logic.message_sender.set_message(f"{err}")

    display_current_db()


    
def display_current_db():
    myserver.execute('SELECT DATABASE()')
    for x in myserver:
        ui.db_display_text.insert('1.0', f'{x}\n')


def test_method():
    print('halp')





# test/development
# def display_cursor():
#     for x in mycursor:
#             ui.db_display_text.insert('1.0', f'{x}\n')

#     ui.db_display_text.insert('1.0', f'{mydb}\n')

# END of document
