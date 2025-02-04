name = 'Thais'
idade = 26
profissao = 'programador'
linguagem = 'python'
saldo = 32.545
\
dados = {'name': 'Thais', 'idade': 26}

print('meu nome e %s, tenho %d anos' % (name, idade))


print('meu nome e {}, tenho {} anos'.format(name, idade))
print('meu nome e {0}, tenho {1} anos'.format(name, idade))
print('meu nome e {0}, tenho {1} anos {1} '.format(name, idade))


print('meu nome e {name}, tenho {idade} anos'.format(name=name, idade=idade))
print('meu nome e {name}, tenho {idade} anos e estudo a linguagem {linguagem}'.format(name=name, idade=idade, linguagem=linguagem))


print( 'Nome : {name}, iadae: {idade}'.format(**dados)),   
print(f'meu nome e {name}, tenho {idade} anos e sou {profissao} e estudo a linguagem {linguagem}')


print(f'meu nome e {name}, tenho {idade} anos {saldo:.2f}')
print(f'meu nome e {name}, tenho {idade} anos {saldo:}')

