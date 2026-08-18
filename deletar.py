from utilitario import *

def deletar_usuario():

    id_usuario = input("Digite o ID do usuário que deseja deletar: ")

    if validar_inteiro(id_usuario):
        return False

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    DELETE FROM usuario
    WHERE id = %s
    """

    cursor.execute(sql, (id_usuario,))

    conexao.commit()

    if cursor.rowcount > 0:
        print("Usuário deletado com sucesso!")

    else:
        print("Usuário não encontrado.")

    cursor.close()
    conexao.close()

def deletar_residencia():

    id_residencia = input("Digite o ID da residência que deseja deletar: ")

    if 


    conexao = conectar()
    cursor = conexao.cursor()

    # Verifica se a residência existe
    cursor.execute("""
        SELECT id_residencia
        FROM residencia
        WHERE id_residencia = %s
    """, (id_residencia,))

    residencia = cursor.fetchone()

    if residencia is None:

        print("Residência não encontrada.")

    else:

        cursor.execute("""
            DELETE FROM residencia
            WHERE id_residencia = %s
        """, (id_residencia,))

        conexao.commit()

        print("Residência deletada com sucesso!")

    cursor.close()
    conexao.close()