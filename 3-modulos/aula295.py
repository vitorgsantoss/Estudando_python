import random
from os import system

system('cls')

r_range = random.randrange(start=10,stop=25, step= 3)#gera um número aleatório 
#entre o intervalo pulando de acordo com o step estipulado
# print(r_range)

r_int = random.randint(10,20)# número aleatório no intervalo sem o step
# print(r_int)

r_float = random.uniform(10,30)#gera um número de ponto flutuante no intervalo
# print(f'{r_float:.2f}')



