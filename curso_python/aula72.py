# Exercicios com funcoes

# Crie uma funcao que multiplica todos os argumentos
# nao nomeados recebidos
# Retorne o total para uma variavel e mostre o valor
# da variavel.

# Crie uma funcao fala se um numero eh par ou impar.
# Retorne se o numero eh par ou impar.


def multiplicacao(*args):
    total = 1
    for numero in args:        
        total = total * numero
    return total

print(f'Total:',multiplicacao(1,2,3))


def par_impar(n):
    if int(n) % 2 == 0:
        return f'{n} eh par'
    return f'{n} eh impar'

print(par_impar(3))
print(par_impar(2))
