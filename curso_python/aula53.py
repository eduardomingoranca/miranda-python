"""
enumerate - enumera iteraveis (indices)
"""
# [(0, 'Mary'), (1, 'Helen'), (2, 'Louis'), (3, 'John')]
lista = ['Mary', 'Helen', 'Louis']
lista.append('John')

lista_enumerada = enumerate(lista)

#print(lista_enumerada)
#for item in lista_enumerada:
#    print(item)

#for item in enumerate(lista):
#    print(item)

#for item in enumerate(lista):
#    indice, nome  = item
#    print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

#for tupla_enumerada in enumerate(lista):
#    print('FOR da tupla: ')
#    for valor in tupla_enumerada:
#        print(f'\t{valor}')
