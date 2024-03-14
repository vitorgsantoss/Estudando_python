from dicionario_json import Pessoa, caminho
import json

with open(caminho, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)

p1 = Pessoa(**pessoas[0])
p2 = Pessoa(**pessoas[1])
print(p1)
print(p2)