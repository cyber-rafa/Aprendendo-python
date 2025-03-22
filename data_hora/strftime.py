from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2023-10-20 12:30:20'
mascara_ptbr = '%d/%m/%Y %a'
mascara_en = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascara_ptbr))

data_convertido = datetime.strptime(data_hora_str, mascara_en)
print(data_convertido.strftime(mascara_ptbr))