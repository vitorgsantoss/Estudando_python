def soma(x,y):
    return x+y

def executa(funcao, x):
    def adiar(y):
        return funcao(x,y)
    return adiar

soma_valores = executa(soma,3)
print(soma_valores(4))