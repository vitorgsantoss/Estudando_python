from copy import deepcopy

def exibe_dicio(lista):
    for dicio in lista:
        for chave, valor in dicio.items():
            print(chave,':', valor, end='   ')
        print()
    print()

produtos  = [
    { 'nome' : 'Produto 5' , 'preco' : 10.00 },
    { 'nome' : 'Produto 1' , 'preco' : 22.32 },
    { 'nome' : 'Produto 3' , 'preco' : 10.11 },
    { 'nome' : 'Produto 2' , 'preco' : 105.87 },
    { 'nome' : 'Produto 4' , 'preco' : 69.90 },
]
novos_produtos= [
    {
        **produto, 'preco' : '{:.2f}'.format(produto['preco']*1.1)
    }
    for produto in produtos
]
exibe_dicio(novos_produtos)


produtos_ordenados_por_nome =sorted(deepcopy(produtos), key= lambda item: item['nome'],reverse= True)

exibe_dicio(produtos_ordenados_por_nome)

produtos_ordenados_por_preco = deepcopy(produtos)
produtos_ordenados_por_preco.sort(key= lambda item: item['preco'])
exibe_dicio(produtos_ordenados_por_preco)