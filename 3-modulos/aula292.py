import shutil
from pathlib import Path
import os

os.system('cls')
caminho = Path.home()/'Documents'/'Python'/'files_test'
shutil.rmtree(caminho)
