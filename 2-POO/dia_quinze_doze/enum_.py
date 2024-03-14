from enum import Enum

semana = Enum('Dias',['SEGUNDA', 'TERCA'])

for dia in semana:
    print(dia.value, dia.name)

# print(semana.SEGUNDA.value, semana.SEGUNDA.name)
# print(semana.TERCA.value, semana.TERCA.name)