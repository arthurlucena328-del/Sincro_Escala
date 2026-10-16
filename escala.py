import json
from pathlib import Path

path_bd = Path(__file__).parent / "BD" / "escala_bd.json"


def _carregar_escalas():
    if not path_bd.exists():
        return []

    with open(path_bd, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def _sub_menu_cadastro_escala():
    print("\nVocê gostaria de cadastrar outra escala?\n")
    print("1. Sim ✅")
    print("2. Não ❌\n")

    if input("Escolha uma opção: ") == "1":
        cadastrar_escala()
    else:
        print("Cadastro de escalas finalizado ✅\n")


def _pedir_id():
    try:
        return int(input("Digite o ID da escala que deseja excluir: "))
    except ValueError:
        print("ID inválido. Digite um número.\n")
        return _pedir_id()


def cadastrar_escala():
    escalas = _carregar_escalas()
    nome = input("Digite o nome da escala: ").strip()

    if any(escala["nome"].strip().casefold() == nome.casefold() for escala in escalas):
        print("\nJá existe uma escala com esse nome!\n")
        _sub_menu_cadastro_escala()
        return

    proximo_id = max((escala["id"] for escala in escalas), default=0) + 1
    escalas.append({"id": proximo_id, "nome": nome})

    with open(path_bd, "w", encoding="utf-8") as arquivo:
        json.dump(escalas, arquivo, ensure_ascii=False, indent=4)

    print(f"Escala cadastrada com sucesso: ID: {proximo_id} - NOME: {nome}")
    _sub_menu_cadastro_escala()


def listar_escala():
    escalas = _carregar_escalas()

    if not escalas:
        print("Não há escalas cadastradas.\n")
        return

    for escala in escalas:
        print(f"ID: {escala['id']} - NOME: {escala['nome']}")

    print("")


def excluir_escala():
    escalas = _carregar_escalas()

    if not escalas:
        print("Não há escalas cadastradas.\n")
        return

    listar_escala()
    id_excluir = _pedir_id()
    escala = next((item for item in escalas if item["id"] == id_excluir), None)

    if escala is None:
        print(f"Escala com ID {id_excluir} não encontrada.\n")
        return

    escalas.remove(escala)

    with open(path_bd, "w", encoding="utf-8") as arquivo:
        json.dump(escalas, arquivo, ensure_ascii=False, indent=4)

    print(f"Escala removida com sucesso: ID: {escala['id']} - NOME: {escala['nome']}\n")
