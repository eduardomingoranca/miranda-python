# Metodos de classe + factories (fabricas)
# Sao metodos onde "self" sera "cls", ou seja,
# ao inves de receber a instancia no primeiro
# parametro, receberemos a propria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anastacia', idade)


p1 = Pessoa('John', 34)
p2 = Pessoa.criar_com_50_anos('Helen')
p3 = Pessoa('Anastacia', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()