import mysql.connector

current_db = ""

db1_server = mysql.connector.connect(
    host="localhost",
    user="ashleyth",
    password="1473Pinkship!",
)

db1_query = mysql.connector.connect(
    host="localhost",
    user="ashleyth",
    password="1473Pinkship!",
    database=f"{current_db}"
)




