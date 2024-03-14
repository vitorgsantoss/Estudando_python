from texto import *

def existe(arq):
    try:
        a= open(arq,'rt')
        a.close()
    except:
        return False
    else:
        return True


def criar(arq):
    try:
        a= open(arq,'wt+')
        a.close()
    except:
        print('Tivemos um problema na criação do arquivo')


def gravar(arquivo):
    prod = input('Informe o nome do produto: ')
    valor= leiafloat('Informe o valor do produto: ')
    try:
        a= open(arquivo,'at')
    except:
        print('Tivemos um problema com a gravação de arquivos')
    else:
        a.write(f'{prod};R$ {valor:.2f}\n')
        a.close()
        print(f'Produto {prod} gravado com sucesso')


def mostrar(arquivo):
    try:
        a=open(arquivo,'rt')
    except:
        print('Tivemos um problema ao exibir os produtos')
    else:
        for item in a:
            dado = item.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<33}{dado[1]:>7}')