import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'usuarios.txt', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Nome', 'Idade', 'Sexo'])
        escritor.writerow(['Lucas', '25', 'Masculino'])
        escritor.writerow(['Maria', '30', 'Feminino'])
except IOError as exc:
    print(f'Erro ao abrir o arquivo. {exc}')