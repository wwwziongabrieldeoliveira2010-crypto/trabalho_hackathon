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
    if media_agua > 18000:
        print("Por favor diminua o seu uso de agua o ideal é de menos de 18000 litros por més")
    else:
        print("Parabens o seu consumo de agua estar dentro do ideal")  

    print(f"Energia: {media_energia:.2f} kWh")
    if media_energia > 250:
        print("Por favor diminua o seu uso de energia o ideal é de menos de 250kWh")
    else:
        print("Parabens o seu consumo de energia estar dentro do ideal")

    print(f"Lixo: {media_lixo:.2f} kg")
    if media_lixo > 151:
        print("Por favor diminua a sua quantidade de lixo produzido o ideal é menos de 151kg")
    else:
        print("Parabens a sua quantidade de lixo produzido estar dentro do ideal")

    cursor.close()
    conexao.close()