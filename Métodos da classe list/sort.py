# Ver a lista de traz para frente

linguagens = ['Python', 'Java', 'C#' , 'csharp' , 'Java']
 
linguagens.sort(reverse=True)

print(linguagens)

# --------------------------------------------- ! --------------------------------------------- #

# Ordenar a lista de forma crescente

linguagens = ['Python', 'Java', 'C#' , 'csharp' , 'Java']

linguagens.sort()

print(linguagens)

# --------------------------------------------- ! --------------------------------------------- #

# Ordenar a lista de forma crescente

linguagens = ['Python', 'js', 'C' , 'java' , 'csaharp']

linguagens.sort(key=lambda x: len(x))

print(linguagens)

# --------------------------------------------- ! --------------------------------------------- #

# Ordenar a lista de forma decrescente
linguagens = ['Python', 'js', 'C' , 'java' , 'csaharp'] 

linguagens.sort(key=lambda x: len(x), reverse=True)

print(linguagens)


# --------------------------------------------- ! --------------------------------------------- #

# Ordenar a lista de forma crescente # 

linguagens = ['Python', 'css', 'C#' , 'csharp' , 'Java']

# Ordenar a lista de forma crescente # 
print(sorted(linguagens , key=lambda x: len(x)))


# ordena de forma decrescente
print(sorted(linguagens , key=lambda x: len(x), reverse=True))

