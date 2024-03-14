import random
from os import system

system('cls')

# random.seed(0)#o seed trabalha com os microsegundos da hora para simular uma 
#pseudoaleatoriedade, alterando o valor para um valor fixo, a aleatoridade acaba

clientes = ['Ruan', 'Alef', 'Lyon', 'Jader', 'Mari', 'Negueba']
random.shuffle(clientes)#muda a ordem da lista original
# print(clientes)

clientes_aleatorios = random.sample(clientes,k=3)#gera uma nova 
# lista com a quantidade de elementos informado em k da sua lista antiga de 
#forma aleatória
# print(clientes_aleatorios)

clientes_aleatorios_repitidos = random.choices(clientes, k=3)#gera uma nova 
# lista com a quantidade de elementos informado em k da sua lista antiga de 
#forma aleatória, porém, repete elementos na nova lista
# print(clientes_aleatorios_repitidos)

cliente_aleatorio = random.choice(clientes)#retorna um elemento aleatório da sua
# lista
print(cliente_aleatorio)