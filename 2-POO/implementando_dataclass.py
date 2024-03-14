from dataclasses import dataclass

@dataclass(frozen=True)
class Pessoa():
    nome: str
    idade: int

    

p1 = Pessoa('Vítor', 19)

print(p1)
