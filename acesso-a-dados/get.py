contatos = {

    'amandasilva01.@gmail.com':{ 'nome': 'Amanda', 'telefone': '332-232' }, 

 
}
# Obtém o valor associado à chave 'chave' no dicionário 'contatos'.
# Se a chave não existir, retorna um dicionário vazio {}.
teste = contatos.get('chave', {})

# Imprime o valor obtido acima.
print(teste)



# Obtém o valor associado à chave 'amandasilva01.@gmail.com' no dicionário 'contatos'.
# Se a chave não existir, retorna um dicionário vazio {}.
teste = contatos.get('amandasilva01.@gmail.com', {})

# Imprime o valor obtido acima.
print(teste)
