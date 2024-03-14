import os
import json

def adicionar(item):
    global lista
    lista.append(item)
    print(lista)

def remover():
    global lista, lista2
    if lista == []:
        print('Não há o que remover')
    else:
        lista2.append(lista.pop())
        print(lista)

def refazer():
    global lista, lista2
    if lista2 == []:
        print('Não há o que refazer!')
    else:
        lista.append(lista2.pop())
        print(lista)

def listar(lista):
    for i in lista:
        print(i)

def primeiro():
    try:
        with open('exercício_listar_tarefas.json','r', encoding='utf8') as arquivo:
            dados= json.load(arquivo)
            print(dados)
    except:
        print('Erro ao carregar o arquivo')


lista=[]
lista2= []
while True:
    comando= input('Informe um comando: ')

    tarefas={
        'remover':lambda: remover(),
        'refazer': lambda: refazer(),
        'clear': lambda: os.system("cls"),
        'primeiro': lambda: primeiro(),
        'listar': lambda: listar(lista),
        'adicionar': lambda: adicionar(comando),
    }
    executar = tarefas.get(comando) if tarefas.get(comando) is not None\
        else tarefas['adicionar']
    
    executar()
      
    while True:
        res= input('Deseja continuar?S/N').strip().upper()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
with open('exercício_listar_tarefas.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        lista,
        arquivo,
        ensure_ascii= False,
        indent= 2
    )