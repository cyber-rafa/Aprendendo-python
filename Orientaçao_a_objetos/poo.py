class Carro:
  # Método construtor
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    self.ligado = False
  
  # Métodos da classe
  def ligar(self):
    if not self.ligado:
      self.ligado = True
      print(f"{self.marca} {self.modelo} foi ligado!")
    else:
      print("O carro já está ligado!")
  
  def desligar(self):
    if self.ligado:
      self.ligado = False
      print(f"{self.marca} {self.modelo} foi desligado!")
    else:
      print("O carro já está desligado!")

# Criando objetos (instâncias) da classe
meu_carro = Carro("Toyota", "Corolla")
outro_carro = Carro("Honda", "Civic")

# Usando os métodos
meu_carro.ligar()
meu_carro.ligar()  # Tentando ligar novamente
meu_carro.desligar()