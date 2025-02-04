contatos = {

    'amandasilva01.@gmail.com':{ 'name': 'Amanda', 'telefone': '332-232' },
 
}



contatos['amandasilva01.@gmail.com'].setdefault('name', 'raul')
contatos['amandasilva01.@gmail.com'].setdefault('idade', 30)


print(contatos)

# nao pode passar assim porq nao consequi encontra a lista assim trascrevendo o codigo
contatos.setdefault('name', 'raul')


