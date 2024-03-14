import os
import shutil

os.system('cls')

HOME = os.path.expanduser('~') #Pega o caminho da pasta user da maquina
PASTA = os.path.join(HOME, 'Documents','EXEMPLO')
NOVA_PASTA = os.path.join(HOME, 'Documents' , 'NOVA_PASTA')
os.makedirs(NOVA_PASTA, exist_ok=True) #cria uma nova pasta

for root, dirs, files in os.walk(PASTA):
    for dir in dirs:
        novo_diretorio = os.path.join(root.replace(PASTA, NOVA_PASTA), dir)
        os.makedirs(novo_diretorio, exist_ok=True)
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        novo_caminho_arquivo = os.path.join(root.replace(PASTA, NOVA_PASTA), file)
        shutil.copy(caminho_arquivo, novo_caminho_arquivo) 