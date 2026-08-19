from banco import conectar
from utilitario import *


def cadastrar_agua():

    conexao = conectar()
    cursor = conexao.cursor()

    # ==========================================
    # ID DA RESIDÊNCIA
    # ==========================================

    while True:

        fk_id_residencia = input(
            "Digite o ID da residência: "
        )

        if not validar_inteiro(fk_id_residencia):
            print("Digite um ID válido.")
            continue
        elif verificar_residencia(fk_id_residencia):
                print("Residência encontrada.")
        else:
            print("Essa residência não existe. Digite outro ID.")
            continue

        # Verifica se a residência existe
        sql = """
        SELECT fk_id_usuario
        FROM residencia
        WHERE fk_id_usuario = %s
        """

        cursor.execute(sql, (fk_id_residencia,))

        residencia = cursor.fetchone()

        if residencia:
            break

        print("Essa residência não existe. Digite outro ID.")

    # ==========================================
    # LITROS DE ÁGUA
    # ==========================================

    while True:

        litros = input(
            "Digite a quantidade de água usada em litros: "
        )
        if validar_decimal(litros):

            litros = float(litros)

            if litros > 0:
                break

        print("Digite uma quantidade válida maior que 0.")

    # ==========================================
    # PREÇO
    # ==========================================

    while True:

        preco = input(
            "Digite o preço por litro: "
        )

        if validar_decimal(preco):

            preco = float(preco)

            if preco >= 0:
                break

        print("Digite um preço válido.")

    # ==========================================
    # MÊS
    # ==========================================

    while True:

        mes = input("Digite o mês (1-12): ")

        if validar_inteiro(mes):

            mes = int(mes)

            if 1 <= mes <= 12:
                break

        print("Digite um mês válido.")

    # ==========================================
    # ANO
    # ==========================================

    while True:

        ano = input("Digite o ano: ")

        if validar_inteiro(ano):

            ano = int(ano)

            if ano >= 2000:
                break

        print("Digite um ano válido.")

    # ==========================================
    # INSERIR NO MYSQL
    # ==========================================

    sql = """
    INSERT INTO agua (
        fk_id_residencia,
        litros_de_agua_usados,
        preco_por_litro,
        mes,
        ano
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        fk_id_residencia,
        litros,
        preco,
        mes,
        ano
    )

    cursor.execute(sql, valores)

    conexao.commit()

    print("Consumo de água cadastrado com sucesso!")

    cursor.close()
    conexao.close()



def cadastrar_energia():

    conexao = conectar()
    cursor = conexao.cursor()

    # ==========================================
    # ID DA RESIDÊNCIA
    # ==========================================

    while True:

        fk_id_residencia = input(
            "Digite o ID da residência: "
        )
        if not validar_inteiro(fk_id_residencia):
            print("Digite um ID válido.")
            continue
        elif verificar_residencia(fk_id_residencia):
            print("Residência encontrada.")
            break
        else:
            print("Residência não encontrada.")
            continue

    # ==========================================
    # CONSUMO DE ENERGIA
    # ==========================================

    while True:

        kwh = input(
            "Digite a quantidade de energia usada em kWh: "
        )

        if validar_decimal(kwh):

            kwh = float(kwh)

            if kwh > 0:
                break

        print("Digite uma quantidade válida maior que 0.")

    # ==========================================
    # PREÇO DO KWH
    # ==========================================

    while True:

        preco = input(
            "Digite o preço do kWh: "
        )

        if validar_decimal(preco):

            preco = float(preco)

            if preco >= 0:
                break

        print("Digite um preço válido.")

    # ==========================================
    # MÊS
    # ==========================================

    while True:

        mes = input("Digite o mês (1-12): ")

        if validar_inteiro(mes):

            mes = int(mes)

            if 1 <= mes <= 12:
                break

        print("Digite um mês válido.")

    # ==========================================
    # ANO
    # ==========================================

    while True:

        ano = input("Digite o ano: ")

        if validar_inteiro(ano):

            ano = int(ano)

            if ano >= 2000:
                break

        print("Digite um ano válido.")

    # ==========================================
    # INSERIR NO MYSQL
    # ==========================================

    sql = """
    INSERT INTO energia (
        fk_id_residencia,
        quilowatts_por_hora,
        preco_do_quilowatt_por_hora,
        mes,
        ano
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        fk_id_residencia,
        kwh,
        preco,
        mes,
        ano
    )

    cursor.execute(sql, valores)

    conexao.commit()

    print("Consumo de energia cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def cadastrar_lixo():

    conexao = conectar()
    cursor = conexao.cursor()

    # ==========================================
    # ID DA RESIDÊNCIA
    # ==========================================

    while True:

        fk_id_residencia = input(
            "Digite o ID da residência: "
        )

        if not validar_inteiro(fk_id_residencia):
            print("Digite um ID válido.")
            continue
        elif verificar_residencia(fk_id_residencia):
                print("Residência encontrada.")
                break
        else:
            print("Essa residência não existe. Digite outro ID.")
            continue

    # ==========================================
    # QUANTIDADE DE LIXO
    # ==========================================

    while True:

        quantidade = input(
            "Digite a quantidade de lixo produzida em kg: "
        )

        if validar_decimal(quantidade):

            quantidade = float(quantidade)

            if quantidade > 0:
                break

        print("Digite uma quantidade válida maior que 0.")

    # ==========================================
    # MÊS
    # ==========================================

    while True:

        mes = input("Digite o mês (1-12): ")
        if validar_inteiro(mes):

            mes = int(mes)

            if 1 <= mes <= 12:
                break

        print("Digite um mês válido.")
    
    # ==========================================
    # ANO
    # ==========================================

    while True:

        ano = input("Digite o ano: ")

        if validar_inteiro(ano):

            ano = int(ano)

            if ano >= 2000:
                break

        print("Digite um ano válido.")

    # ==========================================
    # INSERIR NO MYSQL
    # ==========================================

    sql = """
    INSERT INTO lixo (
        fk_id_residencia,
        quilo_de_lixo,
        mes,
        ano
    )
    VALUES (%s, %s, %s, %s)
    """

    valores = (
        fk_id_residencia,
        quantidade,
        mes,
        ano
    )

    cursor.execute(sql, valores)

    conexao.commit()

    print("Produção de lixo cadastrada com sucesso!")

    cursor.close()
    conexao.close()