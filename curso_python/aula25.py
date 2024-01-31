"""
Interpolacao basica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Louis'
preco = 1000.95897643
variavel = '%s, o preco eh R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d eh %08X' % (15, 15))
