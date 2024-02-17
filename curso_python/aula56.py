"""
split e join com list e str
split - divide uma string
join  - une uma string
"""
frase = 'Olha so que, coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
#    print(lista_frases[i].rstrip())
#    print(lista_frases[i].lstrip())
#    print(lista_frases[i].strip())
    lista_frases.append(lista_frases_cruas[i].strip())

#print(lista_frases_cruas)
#print(lista_frases)
#frases_unidas = '-'.join('abc')
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
