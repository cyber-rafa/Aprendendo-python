def criar_carro(modelo, ano, placa, /, *,marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('uno', 1991, 'ABC-123', marca='fiat', motor='1.0', combustivel='gas')