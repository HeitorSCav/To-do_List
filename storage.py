# Projeto TO-DO List

import json

# PERSISTÊNCIA

'''
Função para carregar as tarefas do arquivo myTasks.json. Se o arquivo não existir, retorna uma lista vazia.
Parâmetros:
    - Nenhum
Retorno: 
    - Lista de tarefas (pode ser vazia se o arquivo não existir)
'''
def carregar_arquivo():
    try:
        with open("myTasks.json", "r") as f:
            tarefas = json.load(f)
            return tarefas          # Devolve a lista se o arquivo myTasks.json existe
    except FileNotFoundError:
        return []                 # Devolve lista vazia se não existe
    
    
'''
Função para salvar as tarefas no arquivo myTasks.json.
Parâmetros:
    - tarefas (dict): Lista de tarefas a ser salva
Retorno:        
    - Nenhum
'''
def salvar_arquivo(tarefas):
    with open("myTasks.json", "w") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)     # Escreve as tarefas no arquivo myTasks.json
 