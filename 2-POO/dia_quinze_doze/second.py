'''Módulo atoa'''

nome = 'Vítor'
def funcao(nome):
    '''Retorna o tamanho do nome'''
    return nome, len(nome)

nome2, tamanho = funcao(nome)

print(nome2, tamanho)