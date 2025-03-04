#atribuição de valores ta uma bagunça mais fazendo isso eu consigo entender melhor 

class Estudante:
    escola = 'DIO'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'Nome: {self.nome} - Matricula: {self.matricula} - Escola: {self.escola}'
        

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)         


aluno1 = Estudante('Guilherme', 1)
aluno2 = Estudante('Giovanna', 2)
mostrar_valores(aluno1, aluno2)


#alterando o valor da classe
Estudante.escola = 'python'
aluno3 = Estudante('Chappie', 3)
mostrar_valores(aluno1, aluno2, aluno3)

#alterando o valor do aluno1
aluno1.nome = 'Arthur'
mostrar_valores(aluno1, aluno2, aluno3)




