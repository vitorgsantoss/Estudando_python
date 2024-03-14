# Resolvendo com set
def conta_repitidos_lista(lista):
    repitidos= set()
    for num in lista:
        if num in repitidos:
            return num
        repitidos.add(num)

listas = [
    [1,2,3,2,3],
    [1,2,3,4,5],
    [3,2,1,4,3,2]
]
for lista in listas:
    repitido_lista=conta_repitidos_lista(lista)
    print(repitido_lista if repitido_lista != None else -1)

# Resolvendo com lista
def conta_repitidos_lista(lista):
    repitidos=[]
    for num in lista:
        if num in repitidos:
            return num
        else:
            repitidos.append(num)


for lista in listas:
    repitido_lista= conta_repitidos_lista(lista) if conta_repitidos_lista(lista)!= None else -1
    print(repitido_lista)