import mysql.connector 


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="18062010"
)

cursor = db.cursor()



cursor.execute("CREATE DATABASE IF NOT EXISTS banco")