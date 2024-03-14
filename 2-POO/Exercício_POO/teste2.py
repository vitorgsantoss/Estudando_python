from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str


lista = [Pessoa('Vítor', 'Santos'), Pessoa('Aleatório', 'Barros')]

lista2 = sorted(lista, key= lambda p:p.sobrenome)

print(lista2)