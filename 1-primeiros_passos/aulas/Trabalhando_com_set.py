conjunto1= set()
conjunto2= set()
conjunto1.update((3,4,5,9))
conjunto2.update((2,4,7,8,0,4,9))
print(conjunto1, conjunto2)
uniao = conjunto2|conjunto1
interseccao= conjunto2&conjunto1
diferenca_primeiro_conjunto= conjunto2-conjunto1
diferenca_ambos_conjuntos= conjunto1^conjunto2
print(f'União: {uniao}\nIntersecção: {interseccao}\nDiferença do conjunto 2: {diferenca_primeiro_conjunto}\nDiferença de ambos os conjuntos: {diferenca_ambos_conjuntos}')