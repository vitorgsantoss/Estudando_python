import math
import os
from aula284 import caminho

os.system('cls')

def formata_tamanho(numero, base = 1024):
    escala = ('B', 'KB', 'MB', 'GB', 'TB', 'PB')
    indice = int(math.log(numero, 1024))
    potencia = 1024 ** indice
    numero_completo = round(numero/potencia, 2)
    return f'{numero_completo} {escala[indice]}'

for root, dirs, files in os.walk(caminho):
    for file in files:
        caminho_completo = os.path.join(root, file)
        print(root)
        # size_file = formata_tamanho(os.path.getsize(caminho_completo))
        size_file = (os.stat(caminho_completo))
        size_file = formata_tamanho(size_file.st_size)
        print('    ', file, size_file)