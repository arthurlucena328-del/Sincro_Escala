from pathlib import Path

path_bd = Path("sincro_escala/BD") / "funcionario_bd.txt"
funcionarios = []

def cadastrar_funcionários():
    print("======================================")
    print("     CAFASTRO DE FUNCIONARIOS")
    print("======================================")
    print("")
    funcionário = input("digite o nome do funcionario: ")
    with open(path_bd,"a", encoding="utf-8") as arquivo:
            arquivo.write(f"{funcionário}\n")
    print(f"O nome cadastrado foi: {funcionário}")
    print("======================================")
    print("você gostaria de adicionar um novo funcionário?")
    print("1. Sim ✅")
    print("2. Não ❌")
    seguir_cadastro = input("Escolha uma opção: ")
    print("======================================")
    if seguir_cadastro  == "1":    
        cadastrar_funcionários()
    if seguir_cadastro == "2":
        print("cadastro concluido ✅")
        
def listar_funcionários():
    with open(path_bd,"r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome_limpo = linha.strip()
            if nome_limpo not in funcionarios:   
                funcionarios.append(nome_limpo) 
    
    print("\n".join(funcionarios))
            
def excluir_funcionários():
    listar_funcionários()
    funcionário = input("qual funcionário você deseja deletar: ")
    with open(path_bd,"r", encoding="utf-8") as arquivo:
        nomes = arquivo.readlines()
    with open(path_bd,"w", encoding="utf-8") as arquivo:
        for linha in nomes :
            if linha.strip() == funcionário:
                linha = ""
            arquivo.write(linha)              
