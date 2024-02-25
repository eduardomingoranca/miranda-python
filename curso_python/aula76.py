# Dicionarios em Python (tipo dict)
# Dicionarios sao estruturas de dados do tipo
# par de 'chave' e 'valor'.
# Chaves podem ser consideradas como o 'indice'
# que vimos na lista e podem ser de tipos imutaveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionario.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionarios.
# Imutaveis: str, int, float, bool, tuple
# Mutavel: dict, list
# pessoa = {
#    'nome': 'Wilbur David',
#    'sobrenome': 'Dunlevy',
#    'idade': 18,
#    'altura': 1.8,
#    'endereco': [
#        {'rua': 'tal tal', 'numero': 123},
#        {'rua': 'outra rua', 'numero': 321},
#    ]
#} 
#print(pessoa, type(pessoa))
#pessoa = dict(nome='Wilbur David', sobrenome='Dunlevy')
pessoa = {    
    'nome': 'Wilbur David',
    'sobrenome': 'Dunlevy',
    'idade': 18,
    'altura': 1.8,
    'endereco': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ]
} 
#print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])

