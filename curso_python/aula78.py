# Sets - Conjuntos em Python (tipo set)
# Conjuntos sao ensinados na matematica
# https://brasilescola.uol.com.br/matematica/conjunto.html
# Representados graficamente pelo diagrama de Venn
# Sets em Python sao mutaveis, porem aceitem apenas
# tipos imutaveis como valor interno.

# Criando um set
# set(iteravel) ou {1, 2, 3}
#s1 = set('Paul')
#print(s1, type(s1))
#s1 = set() # vazio
#s1 = {'Paul', 1, 2, 3} # com dados
#print(s1)

# Sets sao eficientes para remover valores duplicados
# de iteraveis.
# - eles nao tem indexes;
# - eles nao garantem ordem;
# - eles sao iteraveis (for, in, not in)
#s1 = {1, 2, 3, 3, 3, 3, 3, 1}
#l1 = [1, 2, 3, 3, 3, 3, 3, 1]
#s1 = set(l1)
#l2 = list(s1)
#s1 = set('John')
#print(s1)
s1 = {1, 2, 3}
#a = b = 1
#print(s1, a, b)
#print(3 not in s1)
#for numero in s1:
#    print(numero)

# Metodos uteis:
# add, update, clear, discard
s1 = set()
s1.add('Louis')
s1.add(1)
s1.update(('Ola mundo', 1, 2, 3, 4))
#s1.clear()    
s1.discard('Ola mundo')
s1.discard('Louis')
#print(s1)

# Operadores uteis:
# uniao | uniao (union) - Une
# interseccao & (intersection) - Itens presentes em ambos
# diferenca - Itens presentes apenas no set da esquerda
# diferenca simetrica ^ - Itens que nao estao em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # union
s3 = s1 & s2 # intersection
s3 = s2 - s1 # difference
s3 = s2 ^ s1 # simetric difference
print(s3)
