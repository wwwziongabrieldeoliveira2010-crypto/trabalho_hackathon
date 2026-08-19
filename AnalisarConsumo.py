from utilitario import *
def Analisar():
    conn = conectar()
    cursor = conn.cursor()
    while True:
        id_residencia = input("Digite o ID da residência que deseja analisar: ")
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
    while True:
        print("1-agua")
        print("2-energia")
        print("3-lixo")
        print("0-sair")
        anali = input("Qual você quer analisar: ")
        if anali == "1":
            cursor.execute("""SELECT *
            FROM agua
            WHERE fk_id_residencia = %s""", (id_residencia,))
            resultado = cursor.fetchall()
            if not resultado:
                print("Nenhum consumo encontrado.")
            else:
                for consumo in resultado:
                    print(f"""ID: {consumo[0]} | ID da residencia: {consumo[1]} | Aguá usada: {consumo[2]}L""")
                    if consumo[2] > 18000:
                        print("Por favor diminua o seu uso de agua o ideal é de menos de 18000 litros por més")
                    else:
                        print("Parabens o seu consumo de agua estar dentro do ideal") 
        elif anali == "2":

            cursor.execute("""SELECT *
            FROM energia
            WHERE fk_id_residencia = %s""", (id_residencia,))
            resultado = cursor.fetchall()
            if not resultado:
                print("Nenhum consumo encontrado.")
            else:
                for consumo in resultado:
                    print(f"""ID: {consumo[0]} | ID da residencia: {consumo[1]} | energia usada: {consumo[2]}kWh""")
                    if consumo[2] > 250:
                        print("Por favor diminua o seu uso de energia o ideal é de menos de 250kWh")
                    else:
                        print("Parabens o seu consumo de energia estar dentro do ideal")

        elif anali == "3":
            cursor.execute("""SELECT *
            FROM lixo
            WHERE fk_id_residencia = %s""", (id_residencia,))
            resultado = cursor.fetchall()
            if not resultado:
                print("Nenhum consumo encontrado.")
            else:
                for consumo in resultado:
                    print(f"""ID: {consumo[0]} | ID da residencia: {consumo[1]} | lixo produzido: {consumo[2]}kg""")
                    if consumo[2] > 151:
                        print("Por favor diminua a sua quantidade de lixo produzido o ideal é menos de 151kg")
                    else:
                        print("Parabens a sua quantidade de lixo produzido estar dentro do ideal")

        elif anali == "0":
            print("Voltado...")
            cursor.close()
            conn.close()
            break
        else:
            print("Opção invalida")
Analisar()