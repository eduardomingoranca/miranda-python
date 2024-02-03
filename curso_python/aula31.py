"""
Flag (Bandeira) - Marcar um local
None = Nao valor
is e is not = eh ou nao eh (tipo, valor, identidade)
id = Identidade
"""

#v1 = 'a'
#v2 = 'b'
#print(id(v1))
#print(id(v2))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faca algo')
else:
    print('Nao faca algo')

#print(passou_no_if, passou_no_if is None)
#print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Nao passou no if')
else:
    print('Passou no if')
