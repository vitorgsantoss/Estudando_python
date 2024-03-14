# Python apresenta problemas com o método copy quando se precisa copiar
#  valores mutáveis
from copy import deepcopy

alunos= {'Vítor': 5,
         'Afonso': 6,
         }
alunos2= alunos.copy()
alunos2['Afonso']= 7
print('Usando copy com valores imutáveis')
print(alunos)
print(alunos2)
# Até aí tudo bem. Agora a partir do momento que eu passo um dado mutável para cópia
# o python linka as listas ao invés de copiar
notas= {
    'Maria': 6.5,
    'João': 9.7,
    'Bárbara':[3.9,5.6]
}
notas2 = notas.copy()
notas2['Bárbara'][1] = 9.4
print('\nUsando copy com valores mutáveis')
print(notas); print(notas2)
# O python altera a nota nos dois dicionários, para evitar isso usamos o deepcopy
notas= {
    'Maria': 6.5,
    'João': 9.7,
    'Bárbara':[3.9,5.6]
}
notas2 = deepcopy(notas)
notas2['Bárbara'][1] = 9.4
print('\nUsando deepcopy com valores mutáveis')
print(notas); print(notas2)