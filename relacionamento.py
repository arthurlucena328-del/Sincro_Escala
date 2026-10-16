import json
from pathlib import Path

from escala import _carregar_escalas
from funcionario import _carregar_funcionarios

path_bd = Path(__file__).parent / "BD" / "participacao_bd.json"


def _carregar_relacoes():
    if not path_bd.exists():
        return []

    with open(path_bd, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def _salvar_relacoes(relacoes):
    with open(path_bd, "w", encoding="utf-8") as arquivo:
        json.dump(relacoes, arquivo, ensure_ascii=False, indent=4)


def _pedir_id(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        print("ID inválido. Digite um número.\n")
        return _pedir_id(mensagem)


def cadastrar_participacao():
    funcionarios = _carregar_funcionarios()
    escalas = _carregar_escalas()

    if not funcionarios:
        print("Não há funcionários cadastrados.\n")
        return
    if not escalas:
        print("Não há escalas cadastradas.\n")
        return

    print("Funcionários:")
    for funcionario in funcionarios:
        print(f"ID: {funcionario['id']} - NOME: {funcionario['nome']}")

    id_funcionario = _pedir_id("Digite o ID do funcionário: ")
    funcionario = next((f for f in funcionarios if f["id"] == id_funcionario), None)
    if funcionario is None:
        print(f"Funcionário com ID {id_funcionario} não encontrado.\n")
        return

    print("\nEscalas:")
    for escala in escalas:
        print(f"ID: {escala['id']} - NOME: {escala['nome']}")

    id_escala = _pedir_id("Digite o ID da escala: ")
    escala = next((e for e in escalas if e["id"] == id_escala), None)
    if escala is None:
        print(f"Escala com ID {id_escala} não encontrada.\n")
        return

    relacoes = _carregar_relacoes()
    relacao = {"funcionario_id": id_funcionario, "escala_id": id_escala}
    if relacao in relacoes:
        print("Essa participação já está cadastrada.\n")
        return

    relacoes.append(relacao)
    _salvar_relacoes(relacoes)
    print(
        f"Participação cadastrada: funcionário {funcionario['nome']} "
        f"na escala {escala['nome']}.\n"
    )


def listar_participacoes():
    relacoes = _carregar_relacoes()
    funcionarios = _carregar_funcionarios()
    escalas = _carregar_escalas()

    if not relacoes:
        print("Não há participações cadastradas.\n")
        return

    for relacao in relacoes:
        funcionario = next(
            (f for f in funcionarios if f["id"] == relacao["funcionario_id"]), None
        )
        escala = next((e for e in escalas if e["id"] == relacao["escala_id"]), None)
        nome_funcionario = funcionario["nome"] if funcionario else "Funcionário removido"
        nome_escala = escala["nome"] if escala else "Escala removida"
        print(
            f"ID funcionário: {relacao['funcionario_id']} - {nome_funcionario} | "
            f"ID escala: {relacao['escala_id']} - {nome_escala}"
        )
    print("")


def excluir_participacao():
    relacoes = _carregar_relacoes()
    if not relacoes:
        print("Não há participações cadastradas.\n")
        return

    listar_participacoes()
    id_funcionario = _pedir_id("Digite o ID do funcionário da participação: ")
    id_escala = _pedir_id("Digite o ID da escala da participação: ")
    relacao = next(
        (
            r for r in relacoes
            if r["funcionario_id"] == id_funcionario and r["escala_id"] == id_escala
        ),
        None,
    )

    if relacao is None:
        print("Essa participação não foi encontrada.\n")
        return

    relacoes.remove(relacao)
    _salvar_relacoes(relacoes)
    print("Participação removida com sucesso.\n")


def menu_participacoes():
    while True:
        print("=== PARTICIPAÇÃO EM ESCALAS ===")
        print("1. Relacionar funcionário e escala")
        print("2. Listar participações")
        print("3. Remover participação")
        print("0. Voltar ao menu principal\n")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_participacao()
        elif opcao == "2":
            listar_participacoes()
        elif opcao == "3":
            excluir_participacao()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.\n")
