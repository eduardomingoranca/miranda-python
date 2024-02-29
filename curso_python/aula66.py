"""
Argumentos nomeados e nao nomeados em funcoes Python
Argumento nomeado tem nome com sinal de igual
Argumento nao nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definicao 
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, 2, z=5)

print(1, 2, 3, sep='-')

