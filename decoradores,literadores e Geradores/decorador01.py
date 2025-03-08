def mensagem(nome):
    print('executanso mensagem')
    return f'Olá {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'Olá {nome}, tudo bem?'

def executa(funcao):
    print('executando')
    return funcao('Maria') 

print(executa(mensagem_longa))   