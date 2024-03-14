# Soletrando palavras
alfabeto= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(*alfabeto, sep='\t')
# Pegando o último elemento de uma lista em um desempacotamento
lista= ['Vítor', 1, 3.4, (2,4,'Algo'), 'Ult']
a, b, *_, last= lista
print(a, last)