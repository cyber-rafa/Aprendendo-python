import functools

def meu_decorador(func):
    @functools.wraps(func)
    def enveloper(*args, **kwargs):
        print("Antes da função ser chamada")
        resultado = func(*args, **kwargs)
        print("Depois da função ser chamada")
        return resultado

    return enveloper    

@meu_decorador
def ola_mundo(nome):
    print(f'ola mundo {nome}')
    return nome.upper()

resultado = ola_mundo('joao')
print(resultado)
