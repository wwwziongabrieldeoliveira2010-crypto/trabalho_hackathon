import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="01t0M31@"
)
cursor = db.cursor()
cursor.execute("""
CREATE DATABASE IF NOT EXISTS sustentavel
""")
cursor.execute("""
USE sustentavel
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS residencia (
    id_residencia INT AUTO_INCREMENT PRIMARY KEY,
    fk_id_usuario INT NOT NULL,
    quantidade_de_residentes INT NOT NULL,
    endereco VARCHAR(255) NOT NULL,

    FOREIGN KEY (fk_id_usuario)
        REFERENCES usuario(id)
        ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS agua (
    id_agua INT AUTO_INCREMENT PRIMARY KEY,

    fk_id_residencia INT NOT NULL,

    litros_de_agua_usados DECIMAL(10,2) NOT NULL,
    preco_por_litro DECIMAL(10,4),

    mes INT NOT NULL,
    ano INT NOT NULL,

    FOREIGN KEY (fk_id_residencia)
        REFERENCES residencia(id_residencia)
        ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS energia (
    id_energia INT AUTO_INCREMENT PRIMARY KEY,

    fk_id_residencia INT NOT NULL,

    quilowatts_por_hora DECIMAL(10,2) NOT NULL,
    preco_do_quilowatt_por_hora DECIMAL(10,4),

    mes INT NOT NULL,
    ano INT NOT NULL,

    FOREIGN KEY (fk_id_residencia)
        REFERENCES residencia(id_residencia)ON DELETE CASCADE)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS lixo (
    id_lixo INT AUTO_INCREMENT PRIMARY KEY,

    fk_id_residencia INT NOT NULL,

    quilo_de_lixo DECIMAL(10,2) NOT NULL,

    mes INT NOT NULL,
    ano INT NOT NULL,

    FOREIGN KEY (fk_id_residencia)
        REFERENCES residencia(id_residencia)
        ON DELETE CASCADE
)
""")
db.commit()
 
print("Banco de dados criado com sucesso!")
print("Tabelas criadas com sucesso!")
 
cursor.close()
db.close()