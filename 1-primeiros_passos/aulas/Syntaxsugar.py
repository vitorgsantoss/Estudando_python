def funcao(func):
    def interna(*args):
        print('1,2,3...')
        resultado = func(*args)
        resultado+=20
        print(resultado)
        return resultado
    return interna

@funcao
def soma(a,b):
    print(f'{soma.__name__}')
    return a+b

print(soma(2,9))

