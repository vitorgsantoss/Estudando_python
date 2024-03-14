def my_repr(self):
    class_name= self.__class__.__name__
    class_dict= self.__dict__
    return f'{class_name} ({class_dict})'

def adiciona(cls):
    cls.__repr__ = my_repr
    return cls

def decorada(metodo):
    def interna(self):
        resultado = metodo(self)
        if 'Terra' in resultado:
            print('Você está em casa!')
        return resultado
    return interna
    

@adiciona
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @decorada
    def falar_nome(self):
        return f'Planeta é {self.nome}'
    
marte = Planeta('Marte')

terra = Planeta('Terra')
print(terra.falar_nome())
print(marte.falar_nome())
