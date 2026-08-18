import mysql.connector


# ==========================================
# CONEXÃO COM O MYSQL
# ==========================================

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA"
)

cursor = conexao.cursor()


# ==========================================
# CRIAR BANCO DE DADOS
# ==========================================

cursor.execute("""
CREATE DATABASE IF NOT EXISTS sustentavel
""")

cursor.execute("""
USE sustentavel
""")




cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    id INT,
    nome VARCHAR(255),

)
""")




cursor.execute("""
CREATE TABLE IF NOT EXISTS residencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    proprietario VARCHAR(255),
    quantidade_de_residentes INT,
    endereco VARCHAR(255)
)
""")



cursor.execute("""
CREATE TABLE IF NOT EXISTS energia (
    id INT,
    id_residencia INT,
    quilowatts_por_hora DECIMAL(10, 2),
    preco_do_quilowatt_por_hora DECIMAL(10, 2),

    FOREIGN KEY (id_residencia)
    REFERENCES residencia(id)
    ON DELETE CASCADE
)
""")



cursor.execute("""
CREATE TABLE IF NOT EXISTS agua (
    id INT,
    id_residencia INT,
    litros_de_agua_usados DECIMAL(10, 2),
    preco_por_litro DECIMAL(10, 2),

    FOREIGN KEY (id_residencia)
    REFERENCES residencia(id)
    ON DELETE CASCADE
)
""")




cursor.execute("""
CREATE TABLE IF NOT EXISTS lixo (
    id INT,
    id_residencia INT,
    quilo_de_lixo DECIMAL(10, 2),
    multa_por_quilo_de_lixo DECIMAL(10, 2),

    FOREIGN KEY (id_residencia)
    REFERENCES residencia(id)
    ON DELETE CASCADE
)
""")




conexao.commit()


print("Banco de dados criado com sucesso!")
print("Tabelas criadas com sucesso!")



cursor.close()
conexao.close()