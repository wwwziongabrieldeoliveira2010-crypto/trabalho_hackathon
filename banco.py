import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="18062010"
    )

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS fazendeiro")

cursor.execute("USE fazendeiro")


# ==========================================
# TABELA DE GRÃOS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS graos (
    id_grao INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(255) UNIQUE NOT NULL
)
""")


# Grãos disponíveis no sistema

tipo = [
    ("Arroz",),
    ("Feijão",),
    ("Milho",),
    ("Trigo",),
    ("Soja",)
]

cursor.executemany("""
INSERT IGNORE INTO graos (tipo)
VALUES (%s)
""", tipo)


# ==========================================
# TABELA FAMÍLIA
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS familia (
    id_familia INT AUTO_INCREMENT PRIMARY KEY,
    sobrenome VARCHAR(255) NOT NULL,
    quantidade_de_membros INT NOT NULL,
    endereco VARCHAR(255) NOT NULL
)
""")


# ==========================================
# TABELA ESTOQUE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS estoque (
    id_estoque INT AUTO_INCREMENT PRIMARY KEY,

    fk_id_familia INT NOT NULL,
    fk_id_grao INT NOT NULL,

    quantidade DECIMAL(12,2) NOT NULL DEFAULT 0,

    FOREIGN KEY (fk_id_familia)
        REFERENCES familia(id_familia)
        ON DELETE CASCADE,

    FOREIGN KEY (fk_id_grao)
        REFERENCES graos(id_grao)
        ON DELETE CASCADE,

    UNIQUE (fk_id_familia, fk_id_grao)
)
""")


# ==========================================
# TABELA LOGS
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id_log INT AUTO_INCREMENT PRIMARY KEY,

    fk_id_familia INT NOT NULL,
    fk_id_grao INT,

    quantidade DECIMAL(12,2),

    acao VARCHAR(255) NOT NULL,

    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (fk_id_familia)
        REFERENCES familia(id_familia)
        ON DELETE CASCADE,

    FOREIGN KEY (fk_id_grao)
        REFERENCES graos(id_grao)
        ON DELETE SET NULL
)
""")


def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="18062010",
        database="fazendeiro"
    )


