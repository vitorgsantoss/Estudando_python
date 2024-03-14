def exibir_dicionario(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

pessoa1= {
    'nome': 'Vítor',
    'sobrenome': 'Santos',
    'idade': 19
}
pessoa2= {
    'nome1': 'Gabrieli',
    'sobrenome1': 'Santos',
    'idade1': 11
}
exibir_dicionario(**pessoa1)
familia= {**pessoa1, **pessoa2}
print(familia)