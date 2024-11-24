tarefas = {}

def adicionar():
    tarefa = input("Digite a tarefa a ser adicionada: ").strip()
    tarefas[len(tarefas) + 1] = tarefa
    print("Tarefa adicionada com sucesso!")

def alterar():
    codigo = int(input("Digite o código da tarefa: "))
    if codigo in tarefas:
        print("1 - Alterar código da tarefa")
        print("2 - Alterar descrição da tarefa")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            novo_codigo = int(input("Digite o novo código: "))
            if novo_codigo in tarefas:
                print("Erro: Código já existente.")
            else:
                tarefas[novo_codigo] = tarefas.pop(codigo)
                print("Código alterado com sucesso!")
        elif opcao == 2:
            nova_descricao = input("Digite a nova descrição: ").strip()
            tarefas[codigo] = nova_descricao
            print("Descrição alterada com sucesso!")
        else:
            print("Opção inválida.")
    else:
        print("Erro: Código de tarefa não encontrado.")

def excluir():
    codigo = int(input("Digite o código da tarefa que deseja excluir: "))
    if codigo in tarefas:
        del tarefas[codigo]
        print("Tarefa excluída com sucesso!")
    else:
        print("Erro: Código de tarefa não encontrado.")

def pesquisar():
    if tarefas:
        print("\nTarefas cadastradas:")
        for codigo, descricao in tarefas.items():
            print(f"Código: {codigo}, Descrição: {descricao}")
    else:
        print("Nenhuma tarefa cadastrada.")

while True:
    print("1 - Adicionar Tarefa")
    print("2 - Alterar Tarefa")
    print("3 - Excluir Tarefa")
    print("4 - Pesquisar Tarefas")
    print("5 - Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        adicionar()
    elif opcao == 2:
        alterar()
    elif opcao == 3:
        excluir()
    elif opcao == 4:
        pesquisar()
    elif opcao == 5:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
