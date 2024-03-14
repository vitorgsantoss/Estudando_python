from dataclasses import dataclass
import json

caminho= 'classe_pessoa.json'

@dataclass
class Pessoa:
    nome: str
    idade: int


p1 = Pessoa('Vítor', 19)
p2 = Pessoa('Luisa', 43)

dados=[p1.__dict__,vars(p2)]


if __name__ == '__main__':
    with open(caminho,'w',encoding='UTF8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii= False, indent=2)
