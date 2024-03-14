from os import system
from pathlib import Path

system('cls')

# caminho_projeto = Path()
# print(caminho_projeto.absolute())#exibe o diretorio do projeto

# caminho_arquivo = Path(__file__)
# print(caminho_arquivo)#exibe o caminho do arquivo
# print(caminho_arquivo.parent.parent)#parent exibe o nome da pasta pai

# novo_caminho = caminho_arquivo.parent / 'novo_caminho'/'arquivo.txt'
# cria uma string de caminho formatada corretamente(funciona de maneira 
# semelhante ao os.path.join)
# print(novo_caminho)
# home = Path.home()#retorna a home da máquina
# print(home / 'desktop')
# mesmo no print a barra / faz com que o python entenda que se trata de um 
# caminho por ser um objeto da classe Path
# arquivo = home / 'Documents'/'Arquivo.txt'#caminho para um novo arquivo
# arquivo.touch()#cria o arquivo do caminho
# arquivo.write_text('Olá mundo!')#escreve uma mensagem única no arquivo(quando
# outra mensagem é escrita, a anterior é excluída)
# print(arquivo.read_text())#retorna o que tem escrito no arquivo
# arquivo.unlink()#exclui o arquivo

files = Path.home()/'Documents'/'Python'/'files_test'
files.mkdir(exist_ok=True)
for i in range(1,11):
    file = files/f'file_{i}.txt'
    if file.exists():
        file.unlink()
    else:
        file.touch()
    file.write_text(f'Arquivo {i}')
