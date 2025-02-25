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


b1 = bicicleta('caloi', 'elite', 'vermelha', 1000)
print(b1.marca)
