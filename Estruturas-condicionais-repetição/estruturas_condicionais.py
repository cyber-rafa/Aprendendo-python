conta_universitaria = True
conta_especial = False

saldo = 1000
saque = 1500
credito_universitario = 500
cheque_especial = 200

if conta_especial:
    if saldo >= saque:
        print('saque efetuado com sucesso') 
    
    elif saque <= (saldo + cheque_especial):
        print('saque efetuado com sucesso com cheque especial')

    else:
        print('saldo insuficiente')

elif conta_universitaria:
        
        if saldo >= saque:
            print('saque efetuado com sucesso')

        elif saque <= (saldo + credito_universitario):
            print('saque efetuado com sucesso com crédito universitário')
        
        else:
            print('saldo insuficiente')