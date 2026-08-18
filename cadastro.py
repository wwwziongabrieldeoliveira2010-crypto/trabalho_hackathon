from utilitario import *


def cadastro_usuario():

    nome = input("Digite o nome do usuário: ")

    if vali_txt(nome):
        conexao = conectar()
        cursor = conexao.cursor()

        sql =("""
        INSERT INTO usuario (nome)
        VALUES (%s)
        """)
        valores = (nome,)
        cursor.execute(sql, valores)

        conexao.commit()

        print("Usuário cadastrado com sucesso!")

        cursor.close()
        conexao.close()




def cadastrar_residencia():

    while True:
        proprietario = input("Digite o id do proprietário: ")
        if validar_inteiro(proprietario):

            quantidade_residentes = input(
            "Digite a quantidade de residentes: "
            )

            try:
                quantidade_residentes = int(quantidade_residentes)

                if quantidade_residentes <= 0:
                    continue

                print("A quantidade deve ser maior que 0.")

            except ValueError:
                print("Digite um número válido.")

        endereco = input("Digite o endereço da residência: ")
        if vali_txt(endereco):

            conexao = conectar()
            cursor = conexao.cursor()

            sql = """
            INSERT INTO residencia
            (proprietario, quantidade_de_residentes, endereco)
            VALUES (%s, %s, %s)
            """

            valores = (
            proprietario,
            quantidade_residentes,
            endereco
            )

            cursor.execute(sql, valores)

            conexao.commit()

            print("Residência cadastrada com sucesso!")

            cursor.close()
            conexao.close()
cadastro_usuario()
cadastrar_residencia()

