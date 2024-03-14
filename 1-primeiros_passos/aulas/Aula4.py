palavra= 'amor'
lista= ['*','*','*','*']
print (lista)

while True:
    letra = input('Digite uma letra:')[0].lower()

    if letra in palavra:
        for i in range (len(palavra)):
            if palavra[i] == letra:
                lista[i]=letra
    else:
        print('Esta letra não está presente na palavra')
    secreta= ''
   
    for i in range(4):
        secreta+= lista[i]
    print('Palavra', secreta)
    if secreta == palavra:
        break

print('Parabéns, você acertou')