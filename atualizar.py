from utilitario import *

def atualizar_usuario():

    while True:
        id_usuario = input("Digite o ID do usuário que deseja atualizar: ")

        if not validar_inteiro(id_usuario):
            print("Digite um ID válido.")
            continue
        id_usuario = int(id_usuario)
        
        if not verificar_usuario(id_usuario):
        
            print("Usuário não encontrado.")
            print("Digite outro ID.")
            continue
        print("Usuário encontrado.")
        break

    while True:
    
            nome = input("Digite o nome do usuário: ")
    
            if vali_txt(nome):
                break
            print("Digite um nome válido.")
    

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE usuario
    SET nome = %s
    WHERE id = %s
    """

    cursor.execute(sql, (nome,id_usuario,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Nome do usuario atuarizado")

def atualizar_residencia():

    print("\n======================================")
    print("        ATUALIZADOR DE RESIDÊNCIA")
    print("======================================")
    while True:
        id_residencia = input("Digite o ID da residência que deseja atualizar: ")
    
        conexao = conectar()
        cursor = conexao.cursor()
    
        cursor.execute("""
            SELECT id_residencia
            FROM residencia
            WHERE id_residencia = %s
        """, (id_residencia,))
    
        residencia = cursor.fetchone()
    
        if residencia is None:
            print("Residência não encontrada.")
            continue
        break
    # ==========================================
    # ID DO USUÁRIO
    # ==========================================

    while True:

        usuario_id = input(
            "Digite o ID do usuário proprietário da residência: "
        )

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
    id_residencia = int(id_residencia)
    sql = """
        UPDATE residencia
        SET fk_id_usuario = %s, quantidade_de_residentes = %s, endereco = %s
        WHERE id_residencia = %s
    """

    valores = (
        usuario_id,
        quantidade_residentes,
        endereco,
        id_residencia,
    )
    cursor.execute(sql, valores)

    conexao.commit()


    print("\nResidência cadastrada com sucesso!")


    cursor.close()
    conexao.close()

    return True

atualizar_residencia()