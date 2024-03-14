import os
import pathlib

register_way = pathlib.Path(__file__).parent / 'nome_aquivo.txt'

if os.path.exists(register_way):
    with open(register_way,'r') as arquivo:
        pass
    os.remove(register_way)
else:
    print('Arquivo não existe')