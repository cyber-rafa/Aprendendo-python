name  = ' RaFaeL Willian'

print(name.upper())
print(name.lower())
print(name.title())
print(name.isalnum())
print(name.isalpha())
print(name.isdecimal())
print(name.startswith('R'))
print(name[:5])

texto = '   Rio de Janeiro     '
print(texto.strip())
print(texto.lstrip()  + '-')
print(texto.rstrip() + '-')

carros = 'gol'
print( '###' + carros + '###')
print(carros.center(10, '#'))
print('-' .join(carros))