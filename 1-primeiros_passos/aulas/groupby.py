from itertools import groupby

def ordena(aluno):
    return aluno['nota']

alunos = [
    {'nome': 'Vítor', 'nota': '10'},
    {'nome': 'Lucas', 'nota': '8'},
    {'nome': 'Matheus', 'nota': '10'},
    {'nome': 'Luiz', 'nota': '7'},
    {'nome': 'Afonso', 'nota': '8'},
    {'nome': 'Victor', 'nota': '10'},
]

alunos=sorted(alunos, key= ordena)
alunos_agrupados= groupby(alunos, key=ordena)
for nota, aluno in alunos_agrupados:
    print(nota)
    for item in aluno:
        print(item)