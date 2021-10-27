from pymongo import MongoClient
import logic
import ui 
from traceback import format_exc

myclient = None

entry = lambda: logic.entry_getter.get_entry()
entry_trunc = lambda: logic.entry_getter.get_entry_trunc()
get_update_table = lambda: logic.entry_getter.get_update_table()
db_name = lambda: logic.result_sender.get_database_name()
cross_1 = lambda: logic.entry_getter.get_cross1()
cross_2 = lambda: logic.entry_getter.get_cross2()

class GlobalCaller():

    # create
    def create_db():

        try:
            mydb = myclient[f"{logic.entry_getter.get_entry_trunc()}"]
            empty_col = mydb["collection"]
            empty_record = { "Key": "Value"}
            empty_col.insert_one(empty_record)
            GlobalCaller.show_all_db()
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

    def show_all_db():
        try:
            dblist = myclient.list_database_names()
            logic.result_sender.set_result(dblist)
            logic.message_sender.set_message(f"All databases displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

    # delete
    def delete_db():
        try:
            myclient.drop_database(f"{entry_trunc()}")
            GlobalCaller.show_all_db()
            logic.message_sender.set_message(f"Succesfully dropped database: {entry()}")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))


    # make db connection
    def connect_to_db():
        global database_name
        try:
            database_name = f"{entry_trunc()}"
            
            database = myclient[database_name]
            full_coll = database.list_collection_names()
        
            logic.result_sender.set_result(full_coll)
            logic.message_sender.set_message(f"Connected to database: {entry()}\nAll contents (if any) displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

        display_db_name()

    # # run language-specific command     
    # def run_command():
    #     try:
    #         com = entry_trunc()
    #         myclient.com
    #         # GlobalCaller.show_all_db()
    #         logic.message_sender.set_message(f"Results (if any) of custom command displayed below:")
    #     except BaseException:
    #         logic.message_sender.set_message(format_exc(1))

    #     # display_current_db()


database_name = ""

def display_db_name():
    
    logic.result_sender.set_database_info(database_name.split())





class DatabaseCaller():

    # read
    def show_tables():
        pass
        # try:
        #     myserver.execute("SHOW TABLES")
        #     logic.result_sender.set_result(myserver)
        #     logic.message_sender.set_message(f"All tables displayed below:")
        # except BaseException:
        #     logic.message_sender.set_message(format_exc(1))






# Development functions - not for usage in program architecture
def test_method():
    # print(ui.command_text.get('1.0', 'end'))
    # print(type(result_sender.results))
    print(type(myclient.database_name))
    print(myclient.database_name.command("find", "{}"))



    # print(ui.update_table_to.get())






# END of document
