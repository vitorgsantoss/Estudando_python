caminho = 'C:\\Users\\Lucas Calzans\\Documents\\Projeto\\Nova pasta\\'
caminho += 'arquivo_um.txt'
# try:
#     arquivo= open(caminho, 'w')
# finally:
#     arquivo.close()
with open(caminho, 'w+', encoding= 'utf8') as arquivo:
    arquivo.write('Vítor Gabriel\nABC')
    # arquivo.seek(0,1)
    # print(arquivo.read())
with open(caminho, 'r') as arquivo:
    print(arquivo.readline())
    print(arquivo.readline())
    print(arquivo.readline())
