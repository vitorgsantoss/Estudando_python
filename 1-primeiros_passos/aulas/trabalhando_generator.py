from sys import getsizeof

generator = (n for n in range (20))
print(getsizeof(generator))
for num in range(10):
    print(next(generator))
print('Generator pausado')
print('Play:', next(generator))

# generator é um iterável, ou seja, não posso acessar seus índices ou seu tamanho, apenas exibir o próximo elemento