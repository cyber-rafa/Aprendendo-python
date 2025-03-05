
from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    pass
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
     
    
    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):

    @property 
    def marca(self):
        return "Samsung"

    def ligar(self):
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a TV")
     
    



class ControleArCondicionado(ControleRemoto):

    @property 
    def marca(self):
        return "LG"
    
    def ligar(self):
        print("Ligando o ar condicionado")

    def desligar(self):
        print("Desligando o ar condicionado")
        

controle = ControleTV()
print(controle.marca)
controle.ligar()
controle.desligar()


controle = ControleArCondicionado()
print(controle.marca)
controle.ligar()
controle.desligar()


