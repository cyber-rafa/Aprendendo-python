from datetime import timedelta, datetime

tipo_carro = 'G' #'M' 'G' 'P'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficara pronto as {data_estimada}")

elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficara pronto as {data_estimada}")

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficara pronto as {data_estimada}")


resultado = datetime(2023, 10, 11, 12, 12, 12) - timedelta(minutes=12)
print(resultado)