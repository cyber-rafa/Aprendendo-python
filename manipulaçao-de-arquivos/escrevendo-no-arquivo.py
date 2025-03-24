arquivo = open('D:/Github/Aprendendo-python/manipulaçao-de-arquivos/test.txt', 'w')

arquivo.write('Escrevendo dados nos arquivos com Python')
arquivo.writelines(['\n', 'Python '])
arquivo.writelines(['rafael ', ' rafael' ])
arquivo.close()