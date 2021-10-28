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

    # create 
    def create_table():
        try:
            database = myclient[database_name]  
            empty_col = database[f"{logic.entry_getter.get_entry_trunc()}"]
            empty_record = { "Key": "Value"}
            empty_col.insert_one(empty_record)
            DatabaseCaller.show_all_tables()
        except Exception:
            logic.message_sender.set_message(format_exc(1))

    # read
    def show_all_tables():
        try:
            database = myclient[database_name]  
            full_coll = database.list_collection_names()
            logic.result_sender.set_result(full_coll)
            logic.message_sender.set_message(f"Connected to database: {db_name()}\nAll contents (if any) displayed below:")
        except Exception:
            logic.message_sender.set_message(format_exc(1))

    def view_table():
        try:
            database = myclient[database_name]  
            col = entry_trunc()
            logic.result_sender.set_result(database[col].find())
            logic.message_sender.set_message(f"All table data displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))

    # NOT WORKING CORRECTLY
    def view_col_names(): # doc.keys() returns dict_keys object. Needs map and reduce function run to get all fields, then dict_keys needs iteration for display
        try:
            database = myclient[database_name]  
            col = entry_trunc()
            query = database[col].find({})

            for doc in query:
                print(doc.keys())
        
            # key_list = query.keys()
            logic.result_sender.set_result(query)
            # print(key_list)
            # myserver.execute(f"SELECT COLUMN_NAME  FROM INFORMATION_SCHEMA.COLUMNS  WHERE TABLE_SCHEMA = {db_name()} AND TABLE_NAME = '{entry_trunc()}'")
            # logic.result_sender.set_result(myserver)
            logic.message_sender.set_message(f"All columns in {entry_trunc()} displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))
    
    # NEEDS REFACTOR TO MONGODB
    # def cross_columns():
    #     try:
    #         myserver.execute(f"SELECT {cross_1()}, {cross_2()} FROM {entry_trunc()}")
    #         logic.result_sender.set_result(myserver)
    #         logic.message_sender.set_message(f"Reference {cross_1()} by {cross_2()} below:")
    #     except BaseException:
    #         logic.message_sender.set_message(format_exc(1))


    # delete
    def delete_table():
        try:
            database = myclient[database_name]  
            col = database[f"{logic.entry_getter.get_entry_trunc()}"]
            col.drop()
            DatabaseCaller.show_all_tables()
        except Exception:
            logic.message_sender.set_message(format_exc(1))

    # update 
    def rename_table():
        try:
            col = entry_trunc()
            database = myclient[database_name]  
            database[col].rename(f"{get_update_table()}")
            DatabaseCaller.show_all_tables()
            logic.message_sender.set_message(f"Table name successfully updated. All tables displayed below:")
        except BaseException:
            logic.message_sender.set_message(format_exc(1))



# Development functions - not for usage in program architecture
def test_method():
    # print(ui.command_text.get('1.0', 'end'))
    # print(type(result_sender.results))
    print(type(myclient.database_name))
    # myclient.database_name.command("db.dropDatabase")



    # print(ui.update_table_to.get())


# END of document
