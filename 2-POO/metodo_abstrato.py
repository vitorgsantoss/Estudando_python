from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self, som):
        self._som = None
        self.som = som

    
    @property
    @abstractmethod
    def som(self,som):
        ...
    

class Cachorro(Animal):

    @property
    def som(self):
        return f'O animal da espécie {__class__.__name__} emite o seguinte som \'{self._som}\''
    
    @som.setter
    def som(self,som):
        self._som = som


cachorro = Cachorro('auauau')
print(cachorro.som)
