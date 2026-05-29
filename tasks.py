# Projeto TO-DO List

from storage import carregar_arquivo, salvar_arquivo

# LÓGICA

'''
Função para adicionar uma nova tarefa.
Parâmetros:
    - titulo (str): Título da tarefa
Retorno:
    - Nenhum
'''
def adicionar_tarefa(titulo):
    tarefas = carregar_arquivo()

    # Normalizações
    titulo = titulo.strip().title()    # Primeira letra de cada palavra maiúscula e remove espaços excedentes

    # Valida "titulo"
    if titulo == "":
        print("\n**O título não pode estar vazio.**\n")
        return
    
    # Gera ID automático
    if len(tarefas) == 0:
        novo_id = 1
    else:
        novo_id = max(tarefa["id"] for tarefa in tarefas) + 1

    nova_tarefa = {
        "id": novo_id, 
        "titulo": titulo, 
        "concluida": False
    }
    
    tarefas.append(nova_tarefa)
    salvar_arquivo(tarefas)
    print("\n**Tarefa adicionada com sucesso!**\n")