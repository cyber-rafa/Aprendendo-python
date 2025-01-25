def sacar(valor):
    saldo = 100

    if saldo >= valor:
        print('Saque efetuado com sucesso')
        print('Saldo atual: ', saldo - valor)

    if saldo < valor:
        print('Saldo insuficiente')
        print('Saldo atual' , saldo)
          

sacar(110)