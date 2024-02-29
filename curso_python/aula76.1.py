# Manipulando chaves e valores em dicionarios
pessoa = {}

##
##

chave = 'nome'
pessoa[chave] = 'John'
pessoa['sobrenome'] = 'Sanders'
#list = []

print(pessoa[chave])

pessoa[chave] = 'Mary'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

#print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NAO EXISTE')
else:
    print(pessoa['sobrenome'])

#print('ISSO Nao vai')        