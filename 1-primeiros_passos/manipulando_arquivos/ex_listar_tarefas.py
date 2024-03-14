import os

def adicionar(item, lista):
    lista.append(item)
    return lista

def remover(lista, lista2):
    if lista == []:
        print('Não há o que remover')
        return lista, lista2
    else:
        lista2.append(lista.pop())
    return lista,lista2

def refazer(lista, lista2):
    if lista2 == []:
        print('Não há o que refazer!')
        return lista, lista2
    else:
        lista.append(lista2.pop())
    return lista,lista2

lista=[]
lista2= []
while True:
    comando= input('Informe um comando: ')

    if comando.strip().lower() == 'remover':
        lista, lista2= remover(lista, lista2)
        print(lista)
    elif comando.strip().lower() =='refazer':
        lista, lista2= refazer(lista, lista2)
        print(lista)
    elif comando.strip().lower() == 'listar':
        print(lista)
    elif comando == 'clear':
        os.system('cls')
    else:
        lista= adicionar(comando,lista)
        print(lista)
    while True:
        res= input('Deseja continuar?S/N').strip().upper()[0]
        if res in 'SN':
            break
    if res == 'N':
        break