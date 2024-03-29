"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop    - Remove do final ou do indice escolhido
    del    - Apaga um indice
    clear  - Limpa a lista
    extend - Estende a lista
    + -      Concatena listas
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
lista.append('Louis')
nome = lista.pop()
lista.append(1233)
del lista[-1]
lista.clear()
lista.insert(0, 5)
#print(lista)

#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])    
lista.append(50)
lista.pop()
lista.append(60)
#ultimo_valor = lista.pop(3)
#print(lista, 'Removido,', ultimo_valor)

#numero = lista[2]
#print(numero)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
#print(lista_a)


"""
Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
"""
nome = 'Louis'
noutra_variavel = nome
nome = 'John'
#print(nome)
#print(noutra_variavel)

lista_a = ['Louis', 'Mary', 1, True, 1.2]
#lista_b = lista_a
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
