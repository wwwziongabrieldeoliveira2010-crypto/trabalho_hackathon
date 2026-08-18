import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="locahost",
    user="root",
    password="18062010"
    )

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS fazendeiro")
cursor.execute("USE fazendeiro")

cursor.execute("""create table if not exists graos (
 id_grao int primary key,
 tipo varchar (255));""")

cursor.execute("""create table if not exists movimento (
 id_movimentacao int,
 id_grao int,
 gramas decimal (10, 2),
 uso  varchar(255),
 FOREIGN KEY (id_grao) REFERENCES graos(id_graos) ON DELETE CASCADE);""")
