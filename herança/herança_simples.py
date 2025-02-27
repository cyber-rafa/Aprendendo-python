class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar_motor(self):
        print('motor ligado')   

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class motocicleta(veiculo):
    pass


class carro(veiculo):
    pass


class caminhao(veiculo):
    def __init__(self, marca, modelo, ano, carregado):
        super().__init__(marca, modelo, ano)
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Não"} está carregado')


moto = motocicleta('honda', 'cb300', 2020)
print(moto)

carro = carro('fiat', 'uno', 2019)
print(carro)

caminhao = caminhao('volvo', 'fh', 2021, True)
print(caminhao)