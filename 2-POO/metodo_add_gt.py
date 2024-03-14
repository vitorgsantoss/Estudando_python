class Pessoa:
    def __new__(cls,*args,**kwargs):
        instancia = super().__new__(Pessoa)
        print('estou no método new')
        return instancia
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __add__(self, other):
        return f'A soma das idade de {self.nome} e {other.nome} é {self.idade + other.idade}'
    
    def __gt__(self,other):
        return self.idade > other.idade


p1 = Pessoa('Vítor', 19)
p2 = Pessoa('Luisa', 43)
print(p1+p2)
print('Vítor é mais velho que Luisa: ', p1>p2)
print('Luisa é mais velha que Vítor: ',p2>p1)