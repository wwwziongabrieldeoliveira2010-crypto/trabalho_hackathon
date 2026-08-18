from utilitario import *
def estoque():

    print("1-Arroz")
    print("2-Feijão")
    print("3-Milho")
    print("4-Trigo")
    print("5-Soja")
    while True:
        produ = input("O que você produz: ")
        if validar_inteiro(produ):
            produ = int(produ)
            break
        else: 
            print("Erro: digite um número inteiro válido.")

    while True:
        quan = input("O quanto você produziu: ")
        if validar_numero(quan):
            quan = float(quan)
            break
        else: 
            print("Erro: digite um número válido.")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO estoque
    (fk_id_estoque, quantidade)
    VALUES (%s, %s)
    """, (produ, quan))
        
    conexao.commit()
    cursor.close()
    conexao.close()
estoque()