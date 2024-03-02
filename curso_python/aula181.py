# random tem geradores de numeros pseudoaleatorios
# Obs.: numeros pseudoaleatorios significa que os numeros
# parecem ser aleatorios, mas na verdade nao sao. Portanto,
# este modulo nao deve ser usado para seguranca ou uso criptografico.
# O motivo disso eh que quando temos uma mesma entrada e um mesmo algoritimo,
# a saida pode ser previsivel.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random

# Funcoes:
# seed
#   -> Inicializa o gerador de random (por isso "numeros pseudoaleatorios")
# random.seed(0)

# random.randrange(inicio, fim, passo)
#   -> Gera um numero inteiro aleatorio dentro de um intervalo especifico
r_range = random.randrange(10, 20, 2)
# print(r_range)

# random.randint(inicio, fim)
#   -> Gera um numero inteiro aleatorio dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(inicio, fim)
#   -> Gera um numero flutuante aleatorio dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
# print(r_uniform)

# random.shuffle(SequenciaMutavel) -> Embaralha a lista original
nomes = ['Louis', 'Mary', 'Helen', 'Jennifer']
# random.shuffle(nomes)
# print(nomes)

# random.sample(Iteravel, k=N)
#   -> Escolhe elementos do iteravel e retorna outro iteravel (nao repete)
novos_nomes = random.sample(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choices(Iteravel, k=N)
#   -> Escolhe elementos do iteravel e retorna outro iteravel (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choice(Iteravel) -> Escolhe um elemento do iteravel
print(random.choice(nomes))