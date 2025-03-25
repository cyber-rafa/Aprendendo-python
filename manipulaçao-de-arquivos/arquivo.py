from pathlib import Path

ROO_PATH = Path(__file__).parent

try:
    arquivo = open(ROO_PATH  / 'novo.diretorio' )
except FileNotFoundError as exc:
    print('O arquivo não foi encontrado')
    print(exc)
except IsADirectoryError as exc:
    print(f'nao foi possivel abrir o arquivo: {exc}')
except IOError as exc:
    print(f'Erro a o abrir o arquivo: {exc}')
except Exception as exc:
    print(f'algum problema ocorreu: ao acessar o arquivo: {exc}')