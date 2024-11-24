
funcionarios = {}
total_funcionarios = 0


def cadastrar():
    nome = input("Digite o nome do funcionário: ").strip()
    cargo = input("Digite o cargo desse funcionário: ").strip()
    funcionarios[len(funcionarios) + 1] = [nome, cargo]
    print("Funcionário cadastrado com sucesso!")


def alterar():
    cod_funcionario = int(input("Digite o código do funcionário que deseja alterar: "))
    
    if cod_funcionario in funcionarios:
        op = input("O que você deseja alterar? Nome (N) ou cargo (C): ").upper().strip()
        
        if op == "N":
            novo_nome = input("Digite o novo nome do funcionário: ").strip()
            if novo_nome == funcionarios[cod_funcionario][0]:
                print("ERRO: Este nome já está cadastrado. Tente novamente.")
            else:
                funcionarios[cod_funcionario][0] = novo_nome
                print("Nome alterado com sucesso!")
        
        elif op == "C":
            novo_cargo = input("Digite o novo cargo do funcionário: ").strip()
            if novo_cargo == funcionarios[cod_funcionario][1]:
                print("ERRO: Este cargo já está cadastrado. Tente novamente.")
            else:
                funcionarios[cod_funcionario][1] = novo_cargo
                print("Cargo alterado com sucesso!")
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("ERRO: Código de funcionário não encontrado.")


def excluir():
    cod_funcionario = int(input("Digite o código do funcionário que deseja excluir: "))
    
    if cod_funcionario in funcionarios:
        op = input("O que você deseja excluir? Nome (N) ou cargo (C): ").upper().strip()
        
        if op == "N":
            funcionarios[cod_funcionario][0] = "NULO"
            print("Nome excluído com sucesso!")
        elif op == "C":
            funcionarios[cod_funcionario][1] = "NULO"
            print("Cargo excluído com sucesso!")
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("ERRO: Código de funcionário não encontrado.")


def pesquisar():
    if funcionarios:
        print("Lista completa de funcionários:")
        for cod, dados in funcionarios.items():
            print(f"Código: {cod}, Nome: {dados[0]}, Cargo: {dados[1]}")
        
        funcionarios_ordenados = sorted(funcionarios.items(), key=lambda x: x[1][0])
        print("Lista de funcionários em ordem alfabética:")
        for cod, dados in funcionarios_ordenados:
            print(f"Código: {cod}, Nome: {dados[0]}, Cargo: {dados[1]}")
        
        print(f"Total de funcionários cadastrados: {len(funcionarios)}")
    else:
        print("Nenhum funcionário cadastrado.")


while True:
    print("-/_____MENU DE OPÇÕES_____\-")
    print("C - Cadastrar")
    print("A - Alterar")
    print("E - Excluir")
    print("P - Pesquisar")
    print("S - Sair")
    print("-/_________________________\-")
    
    op = input("Digite a letra referente à opção desejada: ").upper().strip()

    if op == "C":
        total_funcionarios += 1
        cadastrar()
    elif op == "A":
        alterar()
    elif op == "E":
        excluir()
    elif op == "P":
        pesquisar()
    elif op == "S":
        print("Encerrando o programa...")
        break
    else:
        print("ERRO: Opção inválida.")
