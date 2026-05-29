# Projeto TO-DO List

from tasks import adicionar_tarefa, listar_tarefas, concluir_tarefa, excluir_tarefa

# MAIN

while True:
    print("\n=== TO-DO LIST ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        try:
            id = int(input("ID da tarefa a concluir: "))
            concluir_tarefa(id)
        except ValueError:
            print("\n**ID inválido. Por favor, insira um número inteiro.**\n")
    elif opcao == "4":
        try:
            id = int(input("ID da tarefa a excluir: "))
            excluir_tarefa(id)
        except ValueError:
            print("\n**ID inválido. Por favor, insira um número inteiro.**\n")
    elif opcao == "0":
        break
    else:
        print("\n**Opção inválida. Por favor, escolha uma opção válida.**\n")