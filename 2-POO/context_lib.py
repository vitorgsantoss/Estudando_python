from contextlib import contextmanager

@contextmanager
def my_open(caminho, modo):
    try: 
        print('Abrindo arquivo')
        arquivo = open(caminho,modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu um erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('arquivo_contextlib.txt', 'w') as arquivo:
    arquivo.write('linha1', 123)
