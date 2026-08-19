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
        usuario_id = input("Digite o ID do usuário proprietário da residência: ")

        if not validar_inteiro(usuario_id):
            print("Digite um ID válido.")
            continue

        usuario_id = int(usuario_id)

        if not verificar_usuario(usuario_id):
            print("Usuário não encontrado.")
            continue

        quantidade_residentes = input(
            "Digite a quantidade de residentes: "
        )

        if not validar_inteiro(quantidade_residentes):
            print("Digite uma quantidade válida.")
            continue

        quantidade_residentes = int(quantidade_residentes)

        if quantidade_residentes <= 0:
            print("A quantidade deve ser maior que 0.")
            continue

        endereco = input("Digite o endereço da residência: ")

        if not vali_txt(endereco):
            print("O endereço não pode estar vazio.")
            continue

        # ==============================
        # CONEXÃO COM O MYSQL
        # ==============================

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO residencia
        (quantidade_de_residentes, endereco)
        VALUES (%s, %s)
        """

        valores = (
            quantidade_residentes,
            endereco
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("Residência cadastrada com sucesso!")

        cursor.close()
        conexao.close()

        return True


cadastro_usuario()
cadastrar_residencia()