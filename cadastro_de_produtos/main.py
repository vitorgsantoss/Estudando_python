from sistema import *
from texto import *
from datetime import datetime
hora = datetime.today().hour
min = datetime.today().minute

linha()
print(f' {datetime.today().strftime("%H:%M"):<16}{datetime.today().strftime("%d-%m-%Y"):>22}     ')
arquivo = 'produtos.txt'
if not existe(arquivo):
    criar(arquivo)
while True:
    res= menu(['Mostrar Produtos','Cadastrar Produtos','Sair do Sistema'])
    if res == 3:
        cab(verde('SAINDO DO SISTEMA... VOLTE SEMPRE!'))
        break
    elif res== 2:
        cab('CADASTRO DE PRODUTOS')
        gravar(arquivo)
    else:
        cab('PRODUTOS CADASTRADOS:')
        mostrar(arquivo)