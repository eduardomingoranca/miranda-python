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
s1 = set() # vazio
s1 = {'Paul', 1, 2, 3} # com dados
print(s1)

# Sets sao eficientes para remover valores duplicados
# de iteraveis.
# - eles nao tem indexes;
# - eles nao garantem ordem;
# - eles sao iteraveis (for, in, not in)

# Metodos uteis:
# add, update, clear, discard
