from itertools import product

roupas=[
    ['preta', 'vermelha', 'branca'],
    ['p','m','g'],
    ['algodão', 'poliéster'],
    ['masculina', 'feminina']
]

print(*list(product(*roupas)),sep='\n')