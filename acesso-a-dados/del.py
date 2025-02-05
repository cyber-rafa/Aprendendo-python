contatos = {
    'natalia001.@gmail.com': { 'nome': 'Natalia', 'telefone': '332-222' },
    'rodrigues01.@gmail.com': { 'nome': 'Rodrigues', 'telefone': '332-221' },
    'amandasilva01.@gmail.com': { 'nome': 'Amanda', 'telefone': '332-232' },
}

del contatos['natalia001.@gmail.com']['telefone']

del contatos['rodrigues01.@gmail.com']

print(contatos)
