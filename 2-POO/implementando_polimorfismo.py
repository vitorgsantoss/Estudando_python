from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def emitir_som(self) -> str:
        ...

class Cachorro(Animal):
    def emitir_som(self,som) -> str:
        return f'Cachorro é capaz de {som}'
    
class Gato(Animal):
    def emitir_som(self,som) -> str:
        return f'Gato é capaz de {som}'
    
lulu = Cachorro()
menina = Gato()

print(lulu.emitir_som('latir'))
print(menina.emitir_som('miar'))