from pathlib import Path

path_bd = Path("Sincro_Escala/BD") / "funcionario_bd.txt" 
funcionarios = []
sair_do_sistema = False

def apresenta_menu():
    print("======================================")
    print("     SISTEMA DE GESTÃO DE ESCALAS")
    print("======================================")
    print("")
    print("1. Cadastrar funcionário📝")
    print("2. Listar funcionário📝📝")
    print("0. Sair ❌")
    print("")
    opcao_menu = input("Escolha uma opção: ")
    return opcao_menu

def cadastrar_funcionário():
    funcionário = input("digite o nome do funcionario: ")
    with open(path_bd,"a", encoding="utf-8") as arquivo:
        arquivo.write(f"{funcionário}\n")
    funcionarios.append(funcionário)
    print(f"O nome cadastrado foi: {funcionário}")
    print("======================================")
    print("você gostaria de adicionar um novo funcionário?")
    print("1. Sim ✅")
    print("2. Não ❌")
    seguir_cadastro = input("Escolha uma opção: ")
    print("======================================")
    if seguir_cadastro  == "1":    
        cadastrar_funcionário()
    if seguir_cadastro == "2":
        print("cadastro concluido ✅")
     
def listar_funcionarios():
    with open(path_bd,"r", encoding="utf-8") as arquivo:
      for linha in arquivo:
            nome_limpo = linha.strip()
            print(nome_limpo)   
   
def sair():
    print("saindo do sistema de gestão de escala⏏️")
#=======================================================================
while not sair_do_sistema: 
    opcao_menu = apresenta_menu()

    match opcao_menu:
        case "1":
            cadastrar_funcionário()
        case "2":
            listar_funcionarios()
        case "0":
            sair()
            break
        case _:
            print("Opção Inválida.")
        
