from utilitario import conectar


def cadastrar_gastos():

    print("\n========================================")
    print("        CADASTRO DE CONSUMO")
    print("========================================")

    id_residencia = int(
        input("Digite o ID da residência: ")
    )

    conexao = conectar()
    cursor = conexao.cursor()

    # ======================================
    # VERIFICAR RESIDÊNCIA
    # ======================================

    cursor.execute("""
        SELECT id_residencia
        FROM residencia
        WHERE id_residencia = %s
    """, (id_residencia,))

    residencia = cursor.fetchone()

    if residencia is None:

        print("Residência não encontrada.")

        cursor.close()
        conexao.close()

        return

    # ======================================
    # ÁGUA
    # ======================================

    print("\n========== ÁGUA ==========")

    agua1 = float(input("Semana 1 (litros): "))
    agua2 = float(input("Semana 2 (litros): "))
    agua3 = float(input("Semana 3 (litros): "))
    agua4 = float(input("Semana 4 (litros): "))

    media_agua = (
        agua1 +
        agua2 +
        agua3 +
        agua4
    ) / 4

    # ======================================
    # ENERGIA
    # ======================================

    print("\n========== ENERGIA ==========")

    energia1 = float(input("Semana 1 (kWh): "))
    energia2 = float(input("Semana 2 (kWh): "))
    energia3 = float(input("Semana 3 (kWh): "))
    energia4 = float(input("Semana 4 (kWh): "))

    media_energia = (
        energia1 +
        energia2 +
        energia3 +
        energia4
    ) / 4

    # ======================================
    # LIXO
    # ======================================

    print("\n========== LIXO ==========")

    lixo1 = float(input("Semana 1 (kg): "))
    lixo2 = float(input("Semana 2 (kg): "))
    lixo3 = float(input("Semana 3 (kg): "))
    lixo4 = float(input("Semana 4 (kg): "))

    media_lixo = (
        lixo1 +
        lixo2 +
        lixo3 +
        lixo4
    ) / 4

    # ======================================
    # SALVAR ÁGUA
    # ======================================

    cursor.execute("""
        INSERT INTO agua (
            fk_id_residencia,
            litros_de_agua_usados
        )
        VALUES (%s, %s)
    """, (
        id_residencia,
        media_agua
    ))

    # ======================================
    # SALVAR ENERGIA
    # ======================================

    cursor.execute("""
        INSERT INTO energia (
            fk_id_residencia,
            quilowatts_por_hora
        )
        VALUES (%s, %s)
    """, (
        id_residencia,
        media_energia
    ))

    # ======================================
    # SALVAR LIXO
    # ======================================

    cursor.execute("""
        INSERT INTO lixo (
            fk_id_residencia,
            quilo_de_lixo
        )
        VALUES (%s, %s)
    """, (
        id_residencia,
        media_lixo
    ))

    conexao.commit()

    print("\n========================================")
    print("       CONSUMO CADASTRADO!")
    print("========================================")

    print(f"Água: {media_agua:.2f} litros")
    print(f"Energia: {media_energia:.2f} kWh")
    print(f"Lixo: {media_lixo:.2f} kg")

    cursor.close()
    conexao.close()