from datetime import datetime
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="01t0M31@"
    )
cursor = db.cursor()

def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="01t0M31@",
        database="sustentavel"
    )
    

def vali_txt(text):
    if text.strip == "":
        print ("Erro: o campo   não pode estar vazio")
        return False

    elif any(text.isdigit() for char in text):
        print ("Erro: campo tem que letra")
        return False
    
    return True 

def vali_num(num1):
    if num1.strip == "":
        print("Error: campo não pode estar vazio")

    try:
        float(num1)
        return True
    except:
        print("Error: o campo tem que ser numero")

def validar_numero(valor):
    if valor.strip == "":
        print ("campo não pode estar vazio")
    try:
        numero = float(valor)

        if numero < 0:
            return False

        return True

    except ValueError:
        return False


def validar_inteiro(valor):

    if valor.strip == "":
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
    VAULES (%s,%s,%s)
    """
    cursor.execute(
        query,
        (
            fk_id_familia,
            acao,
            datetime.now()

        )
    )

    db.commit

    cursor.close()
    db.close 

def ChecarUsuarios():
    while True:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario")
        resultado = cursor.fetchall()
        if not resultado:
            return "Nenhum usuario encontrado."
            break
        else:
            continue
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
lista_usuarios()