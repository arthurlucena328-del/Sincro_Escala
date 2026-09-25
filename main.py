from funcionario import cadastrar_funcionarios, listar_funcionarios, excluir_funcionarios
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
#=======================================================================1
while not sair_do_sistema: 
    opcao_menu = apresenta_menu()

    match opcao_menu:
        case "1":
            cadastrar_funcionarios()
        case "2":
            listar_funcionarios()
        case "3":
            excluir_funcionarios()  
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
        
