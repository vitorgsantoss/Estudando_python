from abc import ABC
import contas

class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade
    
    def __repr__(self):
        return contas.my_repr(self)

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta):
        super().__init__(nome, idade)
        self.conta = conta
