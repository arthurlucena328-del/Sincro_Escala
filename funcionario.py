import json
from pathlib import Path

path_bd = Path(__file__).parent / "BD" / "funcionario_bd.json"
funcionarios = []

def _carregar_funcionarios():
    if not path_bd.exists():
        return []

    with open(path_bd, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def _sub_menu_cadastro_funcionario():
    print("")
    print("Você gostaria de adicionar um novo funcionário?")
    print("")
    print("1. Sim ✅")
    print("2. Não ❌")
    print("")

    seguir_cadastro = input("Escolha uma opção: ")
    print("")

    if seguir_cadastro == "1":    
        cadastrar_funcionarios()
    if seguir_cadastro == "2":
        print("Cadastro finalizado ✅")
        print("")

def _pedir_id():
    try:
        return int(input("Digite o ID do funcionário que deseja excluir: "))
    except ValueError:
        print("ID inválido.\n")
        return _pedir_id()
    
def cadastrar_funcionarios():
    funcionarios = _carregar_funcionarios()
    nome = input("Digite o nome do funcionário: ")

    if any(funcionario["nome"].strip().casefold() == nome.casefold() for funcionario in funcionarios):
        print("")
        print("Já existe um funcionário com esse nome!")
        _sub_menu_cadastro_funcionario()
        return
    
    proximo_id = max((funcionario["id"] for funcionario in funcionarios), default=0) + 1
    funcionarios.append({"id": proximo_id, "nome": nome })

    with open(path_bd, "w", encoding="utf-8") as arquivo:
        json.dump(funcionarios, arquivo, ensure_ascii=False, indent=4)

    print(f"Funcionário cadastrado com sucesso: ID: {proximo_id} - NOME: {nome}")
    _sub_menu_cadastro_funcionario()
        
def listar_funcionarios():
    funcionarios = _carregar_funcionarios()
    for funcionario in funcionarios:
        print(f"ID: {funcionario['id']} - NOME: {funcionario['nome']}")

    print("")
            
def excluir_funcionarios():
    funcionarios = _carregar_funcionarios()

    if not funcionarios:
        print("Não há funcionários cadastrados.")
        return
    
    listar_funcionarios()

    id_excluir = _pedir_id()

    funcionario = next((f for f in funcionarios if f["id"] == id_excluir), None)

    if funcionario is None:
        print(f"Funcionário com ID {id_excluir} não encontrado.")
        print("")
        return

    funcionarios.remove(funcionario)

    with open(path_bd, "w", encoding="utf-8") as arquivo:
        json.dump(funcionarios, arquivo, ensure_ascii=False, indent=4)

    print(f"Funcionário removido com sucesso: ID: {funcionario['id']} - NOME: {funcionario['nome']}")
    print("")

                  
