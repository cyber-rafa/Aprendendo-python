import os 
import shutil
from pathlib import Path

ROO_PATH = Path(__file__).parent

os.mkdir(ROO_PATH / 'novo-diretorio')

arquivo = open(ROO_PATH  / 'novo.txt', 'w')
arquivo.close()

os.rename(ROO_PATH / 'novo.txt', ROO_PATH / 'alterado.txt')

os.remove(ROO_PATH / 'novo.txt')

shutil.move(ROO_PATH / 'alterado.txt', ROO_PATH / 'novo-diretorio' / 'alterado.txt')