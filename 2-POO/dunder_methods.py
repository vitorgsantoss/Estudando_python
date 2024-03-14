class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        classe = type(self).__name__
        return f'{classe}(nome= {self.nome!r}, idade= {self.idade!r})'
    
    def __str__(self):
        return f'({self.nome}, {self.idade})'
    

vitor = Pessoa("Vítor", 19)
gabrieli = Pessoa("Gabrieli", 12)
print(f'{vitor!r}')
print(f'{gabrieli!s}')