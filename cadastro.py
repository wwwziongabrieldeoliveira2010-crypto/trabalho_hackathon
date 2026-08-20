from utilitario import *


# ============================================================
# CADASTRAR USUÁRIO
# ============================================================

def cadastro_usuario():

    print("\n======================================")
    print("          CADASTRO DE USUÁRIO")
    print("======================================")

    while True:

        nome = input("Digite o nome do usuário '0-Para Sair': ")

        if nome == "0":
            print("Voltado...")
            return False
        elif vali_txt(nome):
            break

        print("Digite um nome válido.")


    # ==========================================
    # CONEXÃO COM O MYSQL
    # ==========================================

    conexao = conectar()
    cursor = conexao.cursor()


    # ==========================================
    # INSERIR USUÁRIO
    # ==========================================

    sql = """
        INSERT INTO usuario (nome)
        VALUES (%s)
    """

    valores = (nome,)

    cursor.execute(sql, valores)

    conexao.commit()


    print("\nUsuário cadastrado com sucesso!")


    cursor.close()
    conexao.close()


# ============================================================
# CADASTRAR RESIDÊNCIA
# ============================================================

def cadastrar_residencia():

    print("\n======================================")
    print("        CADASTRO DE RESIDÊNCIA")
    print("======================================")


    # ==========================================
    # ID DO USUÁRIO
    # ==========================================

    while True:

        usuario_id = input(
            "Digite o ID do usuário proprietário da residência '0-Para sair': "
        )

        if usuario_id == "0":
                    print("Voltado...")
                    return False
        if not validar_inteiro(usuario_id):
            print("Digite um ID válido.")
            continue

        usuario_id = int(usuario_id)


        # Verificar se o usuário existe

        if not verificar_usuario(usuario_id):

            print("Usuário não encontrado.")
            print("Digite outro ID.")

            continue


        print("Usuário encontrado.")

        break


    # ==========================================
    # QUANTIDADE DE RESIDENTES
    # ==========================================

    while True:

        quantidade_residentes = input(
            "Digite a quantidade de residentes: "
        )


        if not validar_inteiro(quantidade_residentes):

            print("Digite uma quantidade válida.")

            continue


        quantidade_residentes = int(
            quantidade_residentes
        )


        if quantidade_residentes <= 0:

            print(
                "A quantidade deve ser maior que 0."
            )

            continue


        break


    # ==========================================
    # ENDEREÇO
    # ==========================================

    while True:

        endereco = input(
            "Digite o endereço da residência: "
        )


        if not vali_txt(endereco):

            print(
                "O endereço não pode estar vazio."
            )

            continue


        break


    # ==========================================
    # CONEXÃO COM O MYSQL
    # ==========================================

    conexao = conectar()
    cursor = conexao.cursor()


    # ==========================================
    # INSERIR RESIDÊNCIA
    # ==========================================

    sql = """
        INSERT INTO residencia
        (
            fk_id_usuario,
            quantidade_de_residentes,
            endereco
        )
        VALUES (%s, %s, %s)
    """


    valores = (
        usuario_id,
        quantidade_residentes,
        endereco
    )


    cursor.execute(sql, valores)

    conexao.commit()


    print("\nResidência cadastrada com sucesso!")


    cursor.close()
    conexao.close()

    return True

