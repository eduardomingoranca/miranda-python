"""
Faca um programa que peca ao usuario para digitar um numero inteiro,
informe se este numero eh par ou impar. Caso o usuario nao digite um numero
inteiro, informe que nao eh um numero inteiro.
"""
numero = input('Informe um numero inteiro: ')

try:
    numero_integer = int(numero)
    if numero_integer % 2 == 0:
        print('%d eh par.' % (numero_integer))
    else:
        print('%d eh impar' % (numero_integer))    
except:
    print('valor %s invalido.' % (numero))
