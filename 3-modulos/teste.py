from itertools import groupby

# lista = [
#     {'nome': 'Vítor', 'idade': 19},
#     {'nome': 'Luisa', 'idade': 43},
#     {'nome': 'Everaldo', 'idade': 43},
#     {'nome': 'Gabrieli', 'idade': 12}
# ]

# def ordena(lista):
#     return lista['idade']


# pessoas = sorted(lista, key=ordena)
# agrupadas = groupby(pessoas, key= ordena)

# for chave, valor in agrupadas:
#     print(chave)
#     for pessoa in valor:
#         print(pessoa)

lista=['a', 'a', 'b', 'b', 'c', 'd', 'e', 'f']

def ordena(valor):  
    return valor

lista2 = groupby(lista, key=ordena)

for key,group in lista2:
    print(f'Chave: {key}, grupo: {list(group)}')