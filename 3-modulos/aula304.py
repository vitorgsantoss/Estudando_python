import os
from pathlib import Path
from zipfile import ZipFile
import shutil
# shutil.rmtree(Path(__file__).parent/'aula_186_diretorio_zip')
os.system('clear')

caminho_raiz = Path(__file__).parent
caminho_zip_dir = caminho_raiz / 'aula_304_diretorio_zip'
caminho_arquivo_compactado = caminho_raiz/"arquivo_compactado.zip"
caminho_arquivo_descompactado = caminho_raiz/'arquivo_descompactado'

caminho_zip_dir.mkdir(exist_ok=True)

def criar_arquivos(qtd: int, caminho: Path):
    for i in range(qtd):
        new_file = 'arquivo%s' % i
        with open(caminho/f'{new_file}.txt', 'w') as arquivo:
            arquivo.write(new_file)

criar_arquivos(10,caminho_zip_dir)
with ZipFile(caminho_arquivo_compactado, 'w') as zip:
    for root, dirs, files in os.walk(caminho_zip_dir):
        for file in files:
            zip.write(os.path.join(root,file),file)

with ZipFile(caminho_arquivo_compactado,'r') as zip:
    zip.extractall()


