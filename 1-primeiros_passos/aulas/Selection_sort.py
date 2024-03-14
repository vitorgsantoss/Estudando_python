def selection_sort(lista):
    lista_ordenada=[]
    for i in range(len(lista)):
        menor= lista[0]
        for j in range(len(lista)):
            if menor>=lista[j]:
                menor= lista[j]
        lista_ordenada.append(menor)
        del lista[lista.index(menor)]
    return lista_ordenada


lista=[5,6,2,3,4,9]
print(selection_sort(lista))