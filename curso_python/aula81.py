# Introducao a funcao lambda (funcao anonima de uma linha)
# A funcao lambda eh uma funcao como qualquer
# outra em Python. Porem, sao funcoes anonimas
# que contem apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressao.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Louis', 'sobrenome': 'milford'},
    {'nome': 'Mary', 'sobrenome': 'Olsen'},
    {'nome': 'Daniel', 'sobrenome': 'Silversford'},
    {'nome': 'Edward', 'sobrenome': 'Moncton'},
    {'nome': 'Alice', 'sobrenome': 'Southbourne'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)