import json

dicio={
    'nome1': 'Vítor', 'idade1': 19,
    'nome2': 'Luisa', 'idade2': 42,
}

with open('arquivo.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        dicio,
        arquivo,
        ensure_ascii= False,
        indent= 2
    )

with open('arquivo.json','r',encoding='utf8') as arquivo:
    pessoas=json.load(arquivo)
print(pessoas)
