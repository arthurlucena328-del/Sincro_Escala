from funcionario import cadastrar_funcionários, listar_funcionários, excluir_funcionários
from escala import cadastrar_escala, listar_escala, excluir_escala

sair_do_sistema = False

def apresenta_menu():
    print("======================================")
    print("     SISTEMA DE GESTÃO DE ESCALAS")
    print("======================================")
    print("")
    print("1. Cadastrar funcionário📝")
    print("2. Listar funcionário📝📝")
    print("3. Excluir funcinário🗑️")
    print("4. Criar escala📈")
    print("5. listar escala📉")
    print("6. excluir_escala")
    print("0. Sair ❌")
    print("")
    opcao_menu = input("Escolha uma opção: ")
    print("\n"*5, end="")
    return opcao_menu
     
def sair():
    print("saindo do sistema de gestão de escala⏏️")
#=======================================================================
while not sair_do_sistema: 
    opcao_menu = apresenta_menu()

    match opcao_menu:
        case "1":
            cadastrar_funcionários()
        case "2":
            listar_funcionários()
        case "3":
            excluir_funcionários()  
        case "4":
            cadastrar_escala()  
        case "5":
            listar_escala()
        case "6":
            excluir_escala()     
        case "0":
            sair()
            break
        case _:
            print("Opção Inválida.")
        
