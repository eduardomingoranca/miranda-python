# Desempacotamento em chamados
# de metodos e funcoes
string = 'ABCD'
lista = ['Mary', 'Helen', 1, 2, 3, 'Edwiges']
tupla = 'Python', 'eh', 'legal'
salas = [
    #  0        1
    ['Mary', 'Helen', ], # 0
    #  0
    ['Eloise', ], # 1
    #   0        1        2
    ['Louis', 'John', 'Esther', (0, 10, 20, 30, 40)], # 2
]

#a, b, *_, ap, u = lista
#print(a, u, ap)

#for nome in lista:
#    print(nome, end='')

#print('Mary', 'Helen', 1, 2, 3, 'Edwiges')
#print(*lista)
#print(*string)
#print(*tupla)

print(*salas, sep='\n')
