from pathlib import Path

path_bd = Path("sincro_escala/BD") / "escala_bd.txt"
escalas = []

def cadastrar_escala():
    escala = input("digite o nome da escala: ")
    with open(path_bd,"a", encoding="utf-8") as arquivo:
            arquivo.write(f"{escala}\n")
    escalas.append(escala)
    print(f"A escala cadastrada foi: {escala}")
    print("======================================")
    print("você gostaria de cadastrar novas escalas?")
    print("1. Sim ✅")
    print("2. Não ❌")
    seguir_escala = input("Escolha uma opção: ")
    print("======================================")
    if seguir_escala == "1":    
        cadastrar_escala()
    if seguir_escala== "2":
        print("escala concluida ✅")
        
def listar_escala():
    with open(path_bd,"r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome_limpo = linha.strip()
            print(nome_limpo) 

def excluir_escala():
    listar_escala()
    escala = input("qual escala você deseja deletar: ")
    with open(path_bd,"r", encoding="utf-8") as arquivo:
        nomes = arquivo.readlines()
    with open(path_bd,"w", encoding="utf-8") as arquivo:
        for linha in nomes :
            if linha.strip() == escala:
                linha = ""
            arquivo.write(linha)                     
            