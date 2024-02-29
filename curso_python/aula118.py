# Problema dos parametros mutaveis em funcoes Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Louis')
adiciona_clientes('Jennifer', cliente1)
adiciona_clientes('Ferdinand', cliente1)
cliente1.append('Edward')

cliente2 = adiciona_clientes('Helen')
adiciona_clientes('Mary', cliente2)

cliente3 = adiciona_clientes('Moacir')
adiciona_clientes('Victoria', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)