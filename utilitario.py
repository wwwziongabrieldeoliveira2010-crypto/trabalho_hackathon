from datetime import datetime
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="18062010",
    )
cursor = db.cursor()

def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="18062010",
        database="sustentavel"
    )
    

def vali_txt(text):
    if text.strip() == "":
        print ("Erro: o campo não pode estar vazio")
        return False

    elif any(char.isdigit() for char in text):
        print ("Erro: campo tem que letra")
        return False
    
    return True 

def validar_numero(valor):
    if valor.strip() == "":
        print ("campo não pode estar vazio")
        return False
    try:
        numero = float(valor)

        if numero < 0:
            return False

        return True
    except ValueError:
        return False


def validar_inteiro(valor):

    if valor.strip() == "":
        print ("campo não pode estar vazio")
    try:
        numero = int(valor)

        if numero < 0:
            return False

        return True

    except ValueError:
        return False



def registrar_logs(fk_id_familia, acao):

    db = conectar()
    cursor = db.cursor()

    query = """
    INSERT INTO logs
    (fk_id_familia,acao,data_hora) 
    VALUES (%s,%s,%s)
    """
    cursor.execute(
        query,
        (
            fk_id_familia,
            acao,
            datetime.now()

        )
    )

    db.commit()

    cursor.close()
    db.close()

def ChecarUsuarios():
    while True:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario")
        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        if not resultado:
            return "Nenhum usuario encontrado."
        
        return resultado
def lista_usuarios():

    print("\n=== Lista de usuarios ===")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    resultado = cursor.fetchall()
    if not resultado:
            print("Nenhum usuario encontrado.")
    else:
        for usuario in resultado:
            print(f"""ID: {usuario[0]} | Nome: {usuario[1]}""")

    cursor.close()
    conn.close()    


def validar_decimal(valor):

    if valor.strip() == "":
        return False

    try:
        float(valor)
        return True

    except ValueError:
        return False


def verificar_residencia(id_residencia):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_residencia
        FROM residencia
        WHERE id_residencia = %s
    """, (id_residencia,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado is not None




def verificar_usuario(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id
        FROM usuario
        WHERE id = %s
    """, (id_usuario,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado is not None