import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="01t0M31@"
    )

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS fazendeiro")
cursor.execute("USE fazendeiro")

cursor.execute("""create table if not exists graos (
 id_grao int AUTO_INCREMENT primary key,
 tipo varchar (255) UNIQUE NOT NULL);""")

tipo = [
    ("Arroz",),
    ("Feijão",),
    ("Milho",),
    ("Trigo",),
    ("Soja",)
]
cursor.executemany("""INSERT IGNORE INTO graos (tipo) VALUES (%s)""", tipo)

cursor.execute("""CREATE TABLE IF NOT EXISTS estoque (
 id_estoque int primary key,
 fk_id_grao int,
 quantidade float,
 FOREIGN KEY (fk_id_grao) REFERENCES graos(id_grao) ON DELETE CASCADE
 );""")

cursor.execute("""create table if not exists logs (
 id_log int,
 fk_id_grao int,
 quantidade float,
 acao varchar(255),
 data_hora DATETIME,
 FOREIGN KEY (fk_id_grao) REFERENCES graos(id_grao) ON DELETE CASCADE
 );""")

cursor.execute("""create table if not exists logs (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_graos int,
  usuario varchar(255),
  gramas decimal(10, 2),
  uso varchar(255),
  data datetime,
  FOREIGN KEY (id_grao) REFERENCES graos(id_grao) ON DELETE CASCADE
);""")
