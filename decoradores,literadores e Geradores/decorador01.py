def mensagem(nome):
    print('executanso mensagem')
    return f'Olá {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'Olá {nome}, tudo bem?'

def executa(funcao, nome):
    print('executando')
    return funcao(nome) 

print(executa(mensagem, 'thais'))
print(executa(mensagem_longa, 'Lucas'))   