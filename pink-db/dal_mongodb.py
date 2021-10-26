import pymongo
import ui 

myclient = None

class GlobalCaller():

    def show_all_db():
        dblist = myclient.list_database_names()
        ui.db_display_text.delete('1.0', 'end')

        for x in dblist:
            ui.db_display_text.insert('1.0', f"{x}\n")

    def create_db():
        print('mongodb create!')




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












# END of document
