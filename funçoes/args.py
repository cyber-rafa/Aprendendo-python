def exibir_poema(data_extenso, *lista, **dicionario):
    texto = '\n'.join(lista)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in dicionario.items()])
    mensagem =  f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema(
    'sabado, 01, de janeiro de 1998',
    'O poeta é um fingidor',
    'Finge tão completamente',
    'Que chega a fingir que é dor',
    'A dor que deveras sente.',
    autor='desconhecido',
    ano=1,
)