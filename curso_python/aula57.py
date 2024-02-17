"""
Lista de listas e seus indices
"""
#salas = [
    #  0        1
#    ['Mary', 'Helen', ], # 0
    #  0
#    ['Eloise', ], # 1
    #   0        1        2
#    ['Louis', 'John', 'Esther', (0, 10, 20, 30, 40)], # 2
#]

#print(salas[1][0])
#print(salas[0][1])
#print(salas[2][2])
#print(salas[2][3][2])

salas = [
    #  0        1
    ['Mary', 'Helen', ], # 0
    #  0
    ['Eloise', ], # 1
    #   0        1        2
    ['Louis', 'John', 'Esther', ], # 2
]

for sala in salas:
    print(f'A sala eh {sala}')
    for aluno in sala:
        print(aluno)

