from datetime import datetime
from string import Template
from pathlib import Path
from os import system
import locale

locale.setlocale(locale.LC_ALL,'')

system('cls')

data = datetime.now().date()
caminho = Path(__file__).parent/'aula298.txt'

def converte_para_reais(valor):
    reais = locale.currency(valor, grouping=True)
    return reais

dados = dict(
    nome='Vítor',
    valor=converte_para_reais(1_234_567),
    data = data.strftime('%d/%m/%Y'),
    empresa='V.G - Soluções de Software',
    telefone='+55 4002-8922'
)
with open(caminho, 'w+', encoding='utf8') as arquivo:
    arquivo.writelines('''Prezado(a) $nome,
Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. 
Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone %telefone.

Atenciosamente, ${empresa}.

''')

with open(caminho, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    texto = Template(texto)
    print(texto.substitute(dados))