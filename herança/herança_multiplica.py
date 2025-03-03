# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:
def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    # Lista original de strings
    lista_strings = ["1", "2", "3", "4", "5"]
    
    # 1. Converta cada string na "lista_strings" em um número inteiro utilizando a função "int()"
    # 2. Use a função "map()" para aplicar a função "int()" a cada elemento da "lista_strings"
    # 3. Armazene o resultado em uma variável chamada "elemento"
    elemento = map(int, lista_strings)
    
    # Converte para tupla para usar com soma_tupla
    elementos = tuple(elemento)
    
    # Calcular o resultado
    resultado = soma_tupla(elementos)
    
    # Mostrar o resultado
    print(f"A soma dos elementos da tupla é: {resultado}")
