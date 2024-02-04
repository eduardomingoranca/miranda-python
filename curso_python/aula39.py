"""
Iterando strings com while
"""
#      01234567891011121314
#nome = 'Louis Octavius' # Iteraveis
#      151413121110987654321
#tamanho_nome = len(nome)
#print(nome)
#print(tamanho_nome)
#print(nome[3])

#nova_string += '*L*o*u*i*s* *O*c*t*a*v*i*u*s*'

nome = 'Lon Hammond'

linha = 0
while linha < len(nome):
    print(nome[linha], end='*')
    linha += 1
