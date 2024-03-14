import os
from itertools import count

caminho = r'C:\\Users\\Lucas Calzans\\Documents\\ADS\\4° semestre\\Metodologia'
if __name__ == '__main__':
    os.system('cls')

    counter = count()
    

    for root, dirs, files in os.walk(caminho):
        the_counter = next(counter)
        print(the_counter, 'Pasta atual', root)
        if  len(files) == 0:
            continue
        print('Arquivos:')
        # print(dirs)
        for file in files:
            print('  ', file)