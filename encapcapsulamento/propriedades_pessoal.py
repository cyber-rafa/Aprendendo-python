class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        return 2025 - self._ano_nascimento
    
pessoa = Pessoa("João", 1990)
print(f'Nome: {pessoa.nome} \tidade: {pessoa.idade}')

