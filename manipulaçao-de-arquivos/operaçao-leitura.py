arquivo = open('D:/Github/Aprendendo-python/manipulaçao-de-arquivos/lorem.txt', 'r')


#print(arquivo.readline())#ler a primeira linha

#print(arquivo.readlines())#ler todas as linhas em uma lista

while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()