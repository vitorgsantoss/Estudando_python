'''
importando modulos de outra pasta que não estejam na mesma que o arquivo main
'''
# import sys
# sys.path.append('c:/Users/Lucas Calzans/Downloads/')
# import arquivo


# print('Exibindo o nome do módulo:',__name__)
# print(arquivo.apenas_int(9))
# print(*sys.path, sep='\n')


# recarregando módulos
import importlib
import modulo_teste
for i in range(10):
    importlib.reload(modulo_teste)

