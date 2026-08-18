from utilitario import conectar


def cadastro_usuario():

    nome = input("Digite o nome do usuário: ")

    

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO usuario (nome)
    VALUES (%s)
    """

    valores = (nome)

    cursor.execute(sql, valores)

    conexao.commit()

    print("Usuário cadastrado com sucesso!")

    cursor.close()
    conexao.close()