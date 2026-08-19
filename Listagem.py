from utilitario import *
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

def lista_residencias():

    print("\n=== Lista de residencias ===")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM residencia")
    resultado = cursor.fetchall()
    if not resultado:
            print("Nenhuma residencia encontrado.")
    else:
        for residencia in resultado:
            print(f"""ID da residencia: {residencia[0]} | ID do propriedario: {residencia[1]} | Quantidade de residentes: {residencia[2]} | Endereço: {residencia[3]}""")

    cursor.close()
    conn.close()    

lista_usuarios()
lista_residencias()