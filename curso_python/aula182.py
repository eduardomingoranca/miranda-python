# secrets gera numeros aleatorios seguros
import secrets

# import string as s
# from secrets import SystemRandom as Sr

# print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"

random = secrets.SystemRandom()

# print(secrets.randbelow(100))
# print(secrets.choice([10, 11, 12]))

# Funcoes:
# seed
#   -> NAO FAZ NADA
random.seed(10)

# random.randrange(inicio, fim, passo)
#   -> Gera um numero inteiro aleatorio dentro de um intervalo especifico
r_range = random.randrange(10, 20, 2)
print(r_range)

# random.randint(inicio, fim)
#   -> Gera um numero inteiro aleatorio dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print(r_int)

# random.uniform(inicio, fim)
#   -> Gera um numero flutuante aleatorio dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(r_uniform)

# random.shuffle(SequenciaMutavel) -> Embaralha a lista original
nomes = ['Louis', 'Mary', 'Helen', 'Jennifer']
# random.shuffle(nomes)
print(nomes)

# random.sample(Iteravel, k=N)
#   -> Escolhe elementos do iteravel e retorna outro iteravel (nao repete)
novos_nomes = random.sample(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choices(Iteravel, k=N)
#   -> Escolhe elementos do iteravel e retorna outro iteravel (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choice(Iteravel) -> Escolhe um elemento do iteravel
print(random.choice(nomes))