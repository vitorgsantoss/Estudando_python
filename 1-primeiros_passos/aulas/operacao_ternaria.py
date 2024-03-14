for i in range(4):
    print('Deu certo' if i>2 else 'i é menor que 2')

# colocando condição em uma variável
digito= 10
novo_digito= digito if digito<9 else 0
print(novo_digito)