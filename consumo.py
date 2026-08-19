from utilitario import *


def cadastrar_agua():

    conexao = conectar()
    cursor = conexao.cursor()

    # ==========================================
    # ID DA RESIDÊNCIA
    # ==========================================

    while True:

        fk_id_residencia = input("Digite o ID da residência: ")

        if not validar_inteiro(fk_id_residencia):
            print("Digite um ID válido.")
            continue

        fk_id_residencia = int(fk_id_residencia)

        if verificar_residencia(fk_id_residencia):
            print("Residência encontrada.")
            break

        print("Essa residência não existe.")

    # ==========================================
    # CADASTRO DOS MESES
    # ==========================================

    while True:

        # MÊS
        while True:

            mes = input("Digite o mês (1-12): ")

            if validar_inteiro(mes):

                mes = int(mes)

                if 1 <= mes <= 12:
                    break

            print("Digite um mês válido.")

        # ANO
        while True:

            ano = input("Digite o ano: ")

            if validar_inteiro(ano):

                ano = int(ano)

                if ano >= 2000:
                    break

            print("Digite um ano válido.")

        sql = """
        SELECT id_agua
        FROM agua
        WHERE fk_id_residencia = %s
        AND mes = %s
        AND ano = %s
        """

        cursor.execute(
            sql,
            (fk_id_residencia, mes, ano)
        )

        resultado = cursor.fetchone()

        if resultado:
            print("Esse mês já possui dados cadastrados.")
            continue
        # LITROS
        while True:

            litros = input(
                "Digite a quantidade de água usada em litros: "
            )

            if validar_decimal(litros):

                litros = float(litros)

                if litros > 0:
                    break

            print("Digite uma quantidade válida maior que 0.")

        # PREÇO
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

        print("\nConsumo de água cadastrado com sucesso!")

        # ==========================================
        # PERGUNTAR SE QUER OUTRO MÊS
        # ==========================================

        while True:

            continuar = input(
                "\nDeseja cadastrar outro mês? (s/n): "
            ).lower()

            if continuar == "s":
                break

            elif continuar == "n":
                cursor.close()
                conexao.close()

                print("Cadastro finalizado.")
                return

            else:
                print("Digite apenas S ou N.")



def cadastrar_energia():

    conexao = conectar()
    cursor = conexao.cursor()

    # ==========================================
    # ID DA RESIDÊNCIA
    # ==========================================
    while True:

        fk_id_residencia = input("Digite o ID da residência: ")

        if not validar_inteiro(fk_id_residencia):
            print("Digite um ID válido.")
            continue

        fk_id_residencia = int(fk_id_residencia)

        if verificar_residencia(fk_id_residencia):
            print("Residência encontrada.")
            break

        print("Essa residência não existe.")



    # ==========================================
    # MÊS
    # ==========================================
    while True:

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
                # VERIFICAR SE O MÊS JÁ EXISTE
                # ==========================================

                sql = """
                SELECT id_energia
                FROM energia
                WHERE fk_id_residencia = %s
                AND mes = %s
                AND ano = %s
                """

                cursor.execute(
                    sql,
                    (fk_id_residencia, mes, ano)
                )

                resultado = cursor.fetchone()

                if resultado:
                    print("Esse mês já possui dados cadastrados.")
                    continue

        
        # PEGAR ENERGIA
            while True:

                kwh = input(
                    "Digite a quantidade de energia usada em kWh: "
                )

                if validar_decimal(kwh):

                    kwh = float(kwh)

                    if kwh > 0:
                        break

                print("Digite uma quantidade válida maior que 0.")

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
    
            while True:

                continuar = input(
                    "\nDeseja cadastrar outro mês? (s/n): "
                ).lower()

                if continuar == "s":
                    break

                elif continuar == "n":
                    cursor.close()
                    conexao.close()
                    print("Cadastro finalizado.")
                    return

                else:
                    print("Digite apenas S ou N.")


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

  
    while True:

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


        sql ="""
            SELECT id_energia
            FROM energia
            WHERE fk_id_residencia = %s
            AND mes = %s
            AND ano = %s
            """
        cursor.execute(
            sql,
            (fk_id_residencia, mes, ano)
                )

        resultado = cursor.fetchone()

        if resultado:
            print("Esse mês já possui dados cadastrados.")
            continue

        
        # pegar quantidade de lixo
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