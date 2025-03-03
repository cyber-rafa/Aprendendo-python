class Passaro:
    def voar(self):
        print('Voando...')

class Pardal(Passaro):
    def voar(self):
        super().voar()
        
#um mal exemplo de herança e polimofismo
class Carro(Passaro):
    def voar(self):
        print('Carro não voa')

#um bom exemplo de polimofismo
class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não voa')


#polimofismo vc pode usar o mesmo nome de metodo para diferentes classes
def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Carro())



