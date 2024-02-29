# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, voce so
# precisa herdar de alguma excecao da linguagem.
# A recomendacao da doc eh herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando excecoes (comum colocar Error ao final)
# Levantando (raise) / Lancando (throw) excecoes
# Relancando excecoes
# Adicionando notas em excecoes (3.11.0)
class MeuError(Exception):
    ...