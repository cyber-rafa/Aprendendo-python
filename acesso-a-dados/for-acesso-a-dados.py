contatos = {

    'natalia001.@gmail.com': { 'nome': 'Natalia', 'telefone': '332-222' },
    'rodrigues01.@gmail.com': { 'nome': 'Rodrigues', 'telefone': '332-221' },
    'amandasilva01.@gmail.com':{ 'nome': 'Amanda', 'telefone': '332-232' },
 
}

# Itera sobre os itens do dicionário 'contatos'
for chave, valor in contatos.items():
    # Imprime a chave e o valor de cada item
    print(chave, valor)

# ta  uma bagunça mas é isso ai

contatos2 = {

    'raulsantos01.@gmail.com': { 'nome': 'Raul', 'telefone': '332-422'},

}

print(contatos2)

copia = contatos2.copy()
copia['raulsantos01.@gmail.com'] = {'nome': 'rafael' , 'telefone': '332-422'} 

print(copia)
