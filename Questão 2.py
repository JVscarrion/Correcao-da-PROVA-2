João Vitor Silva Carrion - Turma: 2190

funcionarios = {}

def cadastrar():
    nome = input("Nome do funcionário: ").strip()
    cargo = input("Cargo do funcionário: ").strip()
    funcionarios[len(funcionarios) + 1] = [nome, cargo]
    print("Funcionário cadastrado com sucesso!")

def alterar():
    codigo = int(input("Código do funcionário: "))
    if codigo in funcionarios:
        op = input("Alterar Nome (N) ou Cargo (C)? ").upper().strip()
        if op == "N":
            funcionarios[codigo][0] = input("Novo nome: ").strip()
        elif op == "C":
            funcionarios[codigo][1] = input("Novo cargo: ").strip()
        else:
            print("Opção inválida.")
    else:
        print("Funcionário não encontrado.")

def excluir():
    codigo = int(input("Código do funcionário: "))
    if codigo in funcionarios:
        del funcionarios[codigo]
        print("Funcionário excluído.")
    else:
        print("Funcionário não encontrado.")

def pesquisar():
    if funcionarios:
        for cod, dados in funcionarios.items():
            print(f"Código: {cod}, Nome: {dados[0]}, Cargo: {dados[1]}")
    else:
        print("Nenhum funcionário cadastrado.")

while True:
    print("--/_______MENU DE OPÇÕES_______\--")
    print("C - Cadastrar")
    print("A - Alterar")
    print("E - Excluir")
    print("P - Pesquisar")
    print("S - Sair")
    print("__________________________________")
    
    op = input("Opção: ").upper().strip()
    if op == "C":
        cadastrar()
    elif op == "A":
        alterar()
    elif op == "E":
        excluir()
    elif op == "P":
        pesquisar()
    elif op == "S":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
