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
        print("8 - Atualizar dados da residencia")
        print("9 - Listar usuarios")
        print("10 - Listar residencias")

        opcao = input("digite qual sua opção: ")

        if opcao == "1":
            cadastro_usuario()
        elif opcao == "2":
            cadastrar_residencia()
            
        elif opcao == "3":
            print("1 - Cadastrar consumo de aguá")
            print("2 - Cadastrar consumo de energia")
            print("3 - Cadastrar lixo produzido")
            print("0 - Para sair")
            opcao2 = input("Cadastrar qual consumo: ")
            if opcao2 == "1":
                cadastrar_agua()
            elif opcao2 == "2":
                cadastrar_energia()
            elif opcao2 == "3":
                cadastrar_lixo()
            elif opcao2 == "0":
                print("Voltado...")
            else:
                print("Opção invalida")

        elif opcao == "4":
            Analisar()
        elif opcao == "5":
            deletar_usuario()
        elif opcao == "6":
            deletar_residencia()
        elif opcao == "7":
            atualizar_usuario()
        elif opcao == "8":
            atualizar_residencia()
        elif opcao == "9":
            lista_usuarios()
        elif opcao == "10":
            lista_residencias()
        elif opcao == "0":
            print("saindo do sistema")
            break
        else:
            print(f"{opcao} essa opção é ivalida")
