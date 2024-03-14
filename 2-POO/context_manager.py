class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_, ):
        print('Fechando arquivo')
        self._arquivo.close()
        raise ConnectionError('Não deu para conectar')
        
        # return True #ignorando erro

with MyOpen('criando_context_maneger.txt','w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n',123)
    arquivo.write('Linha 3\n')