import pymongo
import mysql.connector

class Database():
    current_db = ""

    server = mysql.connector.connect(
        host="localhost",
        user="ashleyth",
        password="1473Pinkship!",
    )

    query = mysql.connector.connect(
        host="localhost",
        user="ashleyth",
        password="1473Pinkship!",
        database=f"{current_db}"
    )

db = Database()


# MongoDB Client

myclient = pymongo.MongoClient("mongodb://localhost:27017/")




# END of document
