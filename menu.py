from AnalisarConsumo import *
from atualizar import *
from cadastro import *
from consumo import *
from deletar import *
from Listagem import *

def menu():
    while True:

        print("\n================================")
        print(" SISTEMA DE SUSTENTABILIDADE")
        print("================================")
        print("1 - Cadastrar usuario")
        print("2 - Cadastrar residencia")
        print("3 - Cadastrar gastos")
        print("4 - Mostrar Desempenho Sustentável")
        print("5 - Deletar usuario ")
        print("6 - Deletar residencia")
        print("7 - Atualizar dados da conta")

        opcao = input("digite qual sua opção: ")

        if opcao == "1":
            cadastro_usuario()
        elif opcao == "2":
            cadastrar_residencia()
        elif opcao == "3":
            cadastrar_agua()
            cadastrar_energia()
            cadastrar_lixo()
        elif opcao == "4":
            Analisar()
        elif opcao == "5":
            deletar_usuario()
        elif opcao == "6":
            deletar_residencia()
        elif opcao == "7":
            atualizar_usuario()
        elif opcao == "0":
            print("saindo do sistema")
            break
        else:
            print(f"{opcao} essa opção é ivalida")
