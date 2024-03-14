import csv
from pathlib import Path
from os import system

system('cls')

caminho = Path(__file__).parent/'Arquivo.csv'
# caminho.touch()

# with open(caminho, 'r') as arquivo:
#     leitor = csv.reader(arquivo)
#     for linha in leitor:
#         print(linha)
with open(caminho,'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['Nome'], linha['Idade'])