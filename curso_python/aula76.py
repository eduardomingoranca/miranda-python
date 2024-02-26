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
#print(pessoa['nome'])
#print(pessoa['sobrenome'])

#print()

#for chave in pessoa:
#    print(chave, pessoa[chave])


# Metodos uteis dos dicionarios em Python
# len - quantas chaves
# keys - iteravel com as chaves
# values - iteravel com os valores
# items - iteravel com chaves e valores
# setdefault - adiciona valor se a chave nao existe
# copy - retorna uma copia rasa (shallow copy)
# get - obtem uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o ultimo item adicionado
# update - atualiza um dicionario com outro
p1 = {
    'nome': 'Enoch',
    'sobrenome': 'ben Kohen'
}
#print(p1['nome'])
#print(p1.get('nome', 'Nao existe'))

#nome = p1.pop('nome')
#print(nome)
#print(p1)

#ultima_chave = p1.popitem()
#print(ultima_chave)
#print(p1)

#p1.update({
#    'nome': 'novo valor',
#    'idade': 30
#})
#print(p1)
#p1.update(nome='novo valor', idade=30)
#tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)