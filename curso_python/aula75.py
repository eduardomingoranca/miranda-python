# Exercicios
# Crie funcoes que duplicam, triplicam e quadruplicam
# o numero recebido como parametro.


#def duplicar(numero):
#    return numero * 2


#def triplicar(numero):
#    return numero * 3


#def quadruplicar(numero):
#    return numero * 4


#print('duplicar:', duplicar(3))
#print('triplicar:', triplicar(4))
#print('quadruplicar:', quadruplicar(5))


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(3)
triplicar = criar_multiplicador(4)
quadruplicar = criar_multiplicador(5)

print('duplicar:', duplicar(2))
print('triplicar:', triplicar(3))
print('quadruplicar:', quadruplicar(4))

