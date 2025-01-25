opcao = -1

while opcao != 0:
    opcao = int(input('[1] Para sacar \n[2] para depositar \n[0] para sair : '))
     
    if opcao == 1:
        print('Sacando...') 

    elif opcao == 2:
        print('Depositando...') 







texto = input("Digite um texto: ")
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')

print()






for numero in range(1, 51, 5):
    print(numero, end=' ')

while True:
    numero = int(input('Digite um número:'))

    if numero == 10:
        break

print(numero)





