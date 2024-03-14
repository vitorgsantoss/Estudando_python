from pprint import pprint

lista= [num if num >=4 else 'menor que quatro' for num in range(1,11)]
print(lista)
listas= [
    {'nome': 'Vítor', 'idade': 19},
    {'nome': 'Luisa', 'idade': 42},
    {'nome': 'Everaldo', 'idade': 43},
    {'nome': 'Vitoria', 'idade': 11}
]
familia=[
    {**pessoa, 'idade': pessoa['idade']+1}
    if pessoa['nome'][-1]== 'a' else {**pessoa}#adicionando 1 a idade se o nome terminar com a
    for pessoa in listas
]
pais=[
    {**pessoa} 
    for pessoa in familia 
    if pessoa['idade']>20
]
print(pais)
lista1=[
    [x,i]
    for i in range(1,6)
    for x in range(1,4)
]
pprint(lista1)