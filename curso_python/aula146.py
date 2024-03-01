# Notas das exceptions em Python (add_notes, __notes__)
# https://docs.python.org/3/library/exceptions.html
# Criando excecoes (comum colocar Error ao final)
# Levantando (raise) / Lancando (throw) excecoes
# Relancando excecoes
# Adicionando notas em excecoes (3.11.0)
class MeuError(Exception):
    ...



class OutroError(Exception):
    ...


def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('voce errou isso')
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lancar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error    