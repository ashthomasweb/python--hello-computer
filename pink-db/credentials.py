
import pymongo
import mysql.connector

class Database():
    
    server = mysql.connector.connect(
        host="localhost",
        user="ashleyth",
        password="1473Pinkship!",
        database=''
    )

db = Database()


# MongoDB Client

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# END of document
