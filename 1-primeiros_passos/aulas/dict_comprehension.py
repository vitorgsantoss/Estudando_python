from pprint import pprint

lista=[
    ('Vítor',22),
    ('Augusto',45),
    ('Everaldo',43),
]
dicio= {
    chave:valor
    for chave, valor in lista
}
pprint(dicio)