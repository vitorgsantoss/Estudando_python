from abc import ABCMeta,abstractmethod

class Veiculo (metaclass = ABCMeta):
    def __init__(self,modelo):
        self.modelo = modelo
    
    @abstractmethod
    def mover(self):
        ...


class Moto(Veiculo):
    def mover(self):
        return f'{self.modelo} está se movendo'
    
class Carro(Veiculo):   
    def mover(self):
        return f'{self.modelo} está se movendo'
    

biz = Moto('Biz')
vectra = Carro('Vectra')
print(biz.mover())
print(vectra.mover())