class bicicleta:
    def __init__(self, marca, modelo, cor, valor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.valor = valor

    
    def pedalar(self):
        print('pedalando')

    def buzinar(self):
        print('bi bi')

    def para(self):
        print('parando')
        print('parou')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


b1 = bicicleta('caloi', 'elite', 'vermelha', 1000)
print(b1) 

b2 = bicicleta('monark', 'elite', 'azul', 2000)
print(b2)

b1.pedalar()
b1.buzinar()
b1.para()