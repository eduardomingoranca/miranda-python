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
pessoa = {
    'nome': 'Roy',
    'sobrenome': 'Keppleton',
    'idade': 900
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
#print(len(pessoa))
#print(tuple(pessoa.keys()))
#print(list(pessoa.values()))
#print(list(pessoa.items()))

#for chave in pessoa.keys():
#    print(chave)

#for chave, valor in pessoa.items():
#    print(chave, valor)

