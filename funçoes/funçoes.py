def salvar_carro(modelo, marca, ano, placa):

    print(f'Carro inserido com sucesso! {modelo}/{marca}/{ano}/{placa}')




salvar_carro('Fiat', 'palio', '1991', 'EA-221')
salvar_carro(**{'modelo': 'palio',  'marca': 'fiat', 'ano': '1992' , 'placa': 'TR5-OP' })