from cores import *

def menu(lista):
    cab('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'{verde(c)} - {azul(item)}')
        c+=1
    linha()
    n=valor(len(lista))
    return n

def valor(lst):
    while True:
        try:
            n = int(input('Sua opção: '))
        except(TypeError, ValueError):
            print(vermelho('Erro! Digite um código válido.'))
        else:
            if n>lst or n<1:
                print(vermelho('Erro! Digite um código válido.'))
                continue
            break
    return n

def cab(txt):
    linha()
    print(f'{txt:^40}')
    linha()


def linha(tam=40):
    print('-' * tam)


def leiafloat(msg):
    valido= False
    while not valido:
        n= str(input(msg)).strip().replace(',','.')
        num = n.replace('.', '0')
        if num.isnumeric() and n.count('.') <= 1:
            valido = True
            return float(n)
        else:
            print('Erro! Valor inválido.')
