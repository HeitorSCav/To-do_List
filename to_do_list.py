# Projeto TO-DO List

from tasks import adicionar_tarefa, listar_tarefas, concluir_tarefa, excluir_tarefa, limpar_tela, pausar

# MAIN

while True:
    limpar_tela()
    print("\n=== TO-DO LIST ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        limpar_tela()
        titulo = input("Título da tarefa: ")
        adicionar_tarefa(titulo)
        pausar()
    elif opcao == "2":
        limpar_tela()
        listar_tarefas()
        pausar()
    elif opcao == "3":
        limpar_tela()
        adicionar_tarefa()
        pausar()
    elif opcao == "2":
        limpar_tela()
        listar_tarefas()
        pausar()
    elif opcao == "3":
        limpar_tela()
        try:
            id = int(input("ID da tarefa a concluir: "))
            concluir_tarefa(id)
        except ValueError:
            print("\n**ID inválido. Por favor, insira um número inteiro.**\n")
        pausar()
    elif opcao == "4":
        limpar_tela()
        try:
            id = int(input("ID da tarefa a excluir: "))
            excluir_tarefa(id)
        except ValueError:
            print("\n**ID inválido. Por favor, insira um número inteiro.**\n")
        pausar()
    elif opcao == "0":
        break
    else:
        print("\n**Opção inválida. Por favor, escolha uma opção válida.**\n")
        pausar()
