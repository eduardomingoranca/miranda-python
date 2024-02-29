# class - Classes sao moldes para criar novos objetos
# As classes geram novos objetos (instancias) que
# podem ter seus proprios atributos e metodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar varias acoes.
# Por convencao, usamos PascalCase para nomes de
# classes.
# string = 'Louis'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    ...


p1 = Pessoa('Louis', 'Octavius')
p1.nome = 'Louis'
p1.sobrenome = 'Octavius'

p2 = Pessoa('Mary', 'Jennifer')
p2.nome = 'Mary'
p2.sobrenome = 'Jennifer'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)