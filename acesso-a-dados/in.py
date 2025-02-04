contatos = {
    'natalia001.@gmail.com': { 'nome': 'Natalia', 'telefone': '332-222',},
    'rodrigues01.@gmail.com': { 'nome': 'Rodrigues', 'telefone': '332-221' },
    'amandasilva01.@gmail.com': { 'nome': 'Amanda', 'telefone': '332-232' },
}

reslutado = 'natalia001.@gmail.com' in contatos

print(reslutado)

resultado =  'rafael01@gamil.com' in contatos

print(resultado)

resultado =  'idade'  in contatos['natalia001.@gmail.com']

print(resultado)

resultado = 'telefone' in contatos['rodrigues01.@gmail.com']

print(resultado)