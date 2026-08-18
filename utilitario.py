import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="18062010"
    )
cursor = db.cursor()

def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="18062010",
        database="fazendeiro"
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