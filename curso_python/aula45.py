"""
Iteravel -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next     -> me entregue o proximo valor
iter     -> me entregue seu iterador
"""
#texto = 'Louis'.__iter__()
#texto = iter('Louis') # __iter__()

#print(texto)
#print(texto.__next__())
#print(next(texto))

# for letra in texto
texto = 'Louis' # iteravel
#iterador = iter(texto) # iterator

#while True:
#    try:
#        letra = next(iterador) 
#        print(letra)
#    except StopIteration:
#        break

for letra in texto:
    print(letra)
    