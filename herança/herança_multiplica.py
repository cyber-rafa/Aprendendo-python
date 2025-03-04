class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def ligar(self):
        return f"{self.marca} {self.modelo} está ligado!"

class Voador:
    def __init__(self, altitude_maxima):
        self.altitude_maxima = altitude_maxima
    
    def voar(self):
        return f"Voando a {self.altitude_maxima} metros de altura!"

class CarroVoador(Veiculo, Voador):
    def __init__(self, marca, modelo, altitude_maxima):
        Veiculo.__init__(self, marca, modelo)
        Voador.__init__(self, altitude_maxima)
    
    def mostrar_info(self):
        return f"""
        Carro Voador:
        Marca: {self.marca}
        Modelo: {self.modelo}
        Altitude Máxima: {self.altitude_maxima}m
        """

carro_voador = CarroVoador("FlyingCar", "X-1000", 1000)

print(carro_voador.ligar())
print(carro_voador.voar())
print(carro_voador.mostrar_info())
