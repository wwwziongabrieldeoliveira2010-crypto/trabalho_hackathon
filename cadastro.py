from utilitario import *

def cadastro_familia():

    while True:
        sobrenome = input("Digite o sobrenome de sua família: ")

        if vali_txt(sobrenome):
            break

        else:
            print("Error o campo deve estar campo não pode estar vazio")

    while True:
        residentes = input("Digite o número de pessoas em sua casa: ")

        if validar_inteiro(residentes):
            residentes = int(residentes)
            break

        else: 
            print("Erro: digite um número inteiro válido.")

    while True:
        endereco = input("Digite o endereço de sua fazenda: ")

        if endereco.strip() != "":
            break

        else:
         print("Erro: o endereço não pode estar vazio.")

    conexao = conectar()
    cursor = conexao.cursor()
    query = """INSERT INTO familia (sobrenome,  quantidade_de_membros, endereco) VALUES (%s,%s,%s)"""

    try:

        cursor.execute(
            query,
            (
                sobrenome,
                int(float(residentes)),
                endereco
            )
        )
        conexao.commit()
        cursor.close()
        conexao.close()
    except mysql.connector.Error as err:
        print(f"Erro: {err}")


    print("\n===== CADASTRO =====")
    print(f"Sobrenome: {sobrenome}")
    print(f"Residentes: {residentes}")
    print(f"Endereço: {endereco}")

cadastro_familia()