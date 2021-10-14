import pymongo
import ui 

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# needs to be an object with 
def show_all_db():
    dblist = myclient.list_database_names()
    ui.db_display_text.delete('1.0', 'end')

    for x in dblist:
        ui.db_display_text.insert('1.0', f"{x}\n")