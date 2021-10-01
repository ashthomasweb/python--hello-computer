import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ashleyth",
  password="1473Pinkship!"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabasetest")