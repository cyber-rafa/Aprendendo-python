from pathlib import Path 

ROOT_PATH = Path(__file__).parent

#try:
    #with open(ROOT_PATH / 'arquivo-utf--8', 'w', encoding='utf-8') as arquivo:
            #arquivo.write('Escrevendo dados nos arquivos com Python')
#except FileNotFoundError as exc:
      #print('Erro ao abrir o arquivo')

try:
    with open(ROOT_PATH / 'arquivo-utf--8', 'r', encoding='ascii') as arquivo:
            arquivo.write('Escrevendo dados nos arquivos com Python')
except IOError as exc:
      print('Erro ao abrir o arquivo')
except UnicodeEncodeError as exc:
      print(exc)