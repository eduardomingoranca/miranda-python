# Operadores in e not in
# Strings sao iteraveis
# 0 1 2 3 4 5 6 7
# O c t a v i u s
#-8-7-6-5-4-3-2-1
#nome = 'Octavius'
#print(nome[2])
#print(nome[-4])
#print('a' in nome)
#print('z' in nome)
#print('vius' in nome)
#print('zero' in nome)
#print(10 * '-')
#print('vius' not in nome)
#print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')
        