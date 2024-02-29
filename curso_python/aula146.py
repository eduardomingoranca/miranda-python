# Levantando e tratando suas Exceptions (Excecoes)
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
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lancar de novo')
    raise exception_ from error    