import os

os.system('cls')

caminho = os.path.dirname(os.getcwd())
#pegando o caminho atual sem o último diretório
conteudo_pasta= []
conteudo_pasta.append(os.listdir(caminho))

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho,pasta)
    print(pasta)
    for arquivo in os.listdir(caminho_completo_pasta):
        print('  ', arquivo)

