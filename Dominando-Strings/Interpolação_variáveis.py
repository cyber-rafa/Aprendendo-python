name = 'Thais'
idade = 26
profissao = 'programador'
linguagem = 'python'

print('meu nome e %s, tenho %d anos' % (name, idade))

print('meu nome e {}, tenho {} anos'.format(name, idade))

print('meu nome e {0}, tenho {1} anos'.format(name, idade))
print('meu nome e {0}, tenho {1} anos {1} '.format(name, idade))

print('meu nome e {name}, tenho {idade} anos'.format(name=name, idade=idade))
