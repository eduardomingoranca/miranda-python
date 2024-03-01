# Enum -> Enumeracoes
# Enumeracoes na programacao, sao usadas em ocasioes onde temos
# um determinado numero de coisas para escolher.
# Enums tem membros e seus valores sao constantes.
# Enums em python:
#   - sao um conjunto de nomes simbolicos (membros) ligados a valores unicos
#   - podem ser iterados para retornar seus membros canonicos na ordem de
#       definicao
# enum.Enum eh a superclasse para suas enumeracoes. Mas tambem pode ser usada
#   diretamente (mesmo assim, Enums nao sao classes normais em Python).
# Voce podera usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

def mover(direcao):
    print(f'Movendo para {direcao}')


mover('esquerda')
mover('direita')
mover('acima')
mover('abaixo')