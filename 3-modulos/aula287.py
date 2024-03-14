import shutil
import os

user = os.path.expanduser('~')
pasta = os.path.join(user, 'Documents','EXEMPLO')
destino = os.path.join(user, 'Documents','Python','PASTA_TESTE_AULA287')
NOVA_PASTA = os.path.join(user, 'Documents' , 'NOVA_PASTA')

# if os.path.exists(NOVA_PASTA): 
    # shutil.rmtree(NOVA_PASTA)#exclui a pasta
# os.makedirs(NOVA_PASTA) #cria uma nova pasta
shutil.copytree(pasta,NOVA_PASTA)
shutil.move(NOVA_PASTA, destino)
shutil.rmtree(destino)
