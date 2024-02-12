"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""
#        +01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)
#print(bool([])) # false
#print(lista, type(lista))

#         0     1          2           3    4
lista = [123, True, 'Louis Octavius', 1.2, []]
#print(lista[2].upper(), type(lista[2]))
lista[-3] = 'Mary'
#print(lista)
#print(lista[2], type(lista[2]))

lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])    
lista.append(50)
lista.pop()
lista.append(60)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)

#numero = lista[2]
#print(numero)
