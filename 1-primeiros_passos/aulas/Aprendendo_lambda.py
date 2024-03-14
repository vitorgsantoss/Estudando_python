# lista= [
#     {'nome': 'Vítor', 'sobrenome': 'Santos'},
#     {'nome': 'Matheus', 'sobrenome': 'Vieira'}
# ]
# def ordena(item):
#     print(item)
#     return item['nome']

# lista.sort(key=ordena)
# print(lista)

# lista1= lista.copy()
# lista1.sort(key= lambda item: item['nome'])
# print(lista1)

# generator= {n for n in range(7) }
# par= lambda x : x if x%2==0 else None
# total= list(map(par, generator))
# total= list(filter(lambda x: x is x is not None, total))
# print(total)

# Jeito mais simples de solucionar o exercício acima:
# generator= {n for n in range(1,21)}
# apenas_pares = tuple(filter(lambda x:x%2==0, generator))
# print(apenas_pares)
