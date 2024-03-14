capitais = ['Salvador', 'São Paulo', 'Belo Horizinte']
estados = ['BA', 'SP', 'MG', 'RJ']
def zipper(lista1, lista2):
    resultado=[]
    lista1, lista2 = compara(lista1, lista2)
    for i in range(len(lista1)):
        resultado.append((lista1[i], lista2[i]))
    print(resultado)
        

def compara(lista1, lista2):
    if len(lista1)> len(lista2):
       lista1, lista2 = tamanhos_iguais(lista1,lista2)
    elif len(lista1)< len(lista2):
        lista2, lista1 = tamanhos_iguais(lista2, lista1)
    return lista1, lista2

def tamanhos_iguais(lista1,lista2):
    while True:
        lista1.pop()
        if len(lista1)== len(lista2):
            break
    return lista1,lista2

zipper(capitais, estados)
