import csv
from pathlib import Path
from os import system

system('cls')

caminho = Path(__file__).parent/'Arquivo.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]
with open(caminho,'w', encoding='utf8') as arquivo:
    nome_campos = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo, nome_campos)
    escritor.writeheader()
    
    # for cliente in lista_clientes:
    escritor.writerows(lista_clientes)


# with open(caminho, 'w', encoding='utf8') as arquivo:
#     escritor = csv.writer(arquivo)
#     escritor.writerow(lista_clientes[0].keys())
#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())