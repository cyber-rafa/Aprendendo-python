numeros = {1, 2, 3, 4, 5 , 5, 6, 7, 7, 8, 9, 10}


numeros.discard(1)
numeros.discard(45)

print(numeros)

numeros = {1, 2, 3, 4, 5 , 5, 6, 7, 7, 8, 9, 10}

numeros.remove(7)
numeros.remove(2)

# o remove() gera um erro caso o valor passado como parametro não exista no conjunto
numeros.remove(45)

print(numeros)