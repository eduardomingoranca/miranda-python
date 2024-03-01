# Metaclasses sao o tipo das classes
# EM PYTHON, TUDO EH UM OBJETO (CLASSES TAMBEM)
# Entao, qual eh o tipo de uma classe? (type)
# Seu objeto eh uma instancia da sua classe
# Sua classe eh uma instancia de type (type eh uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrao nessa ordem:
# __new__ da metaclass eh chamado e cria a nova classe
# __call__ da metaclass eh chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instancia)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execuçao
#
# Metodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instancia)
#
# "Metaclasses sao magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se voce quer saber se precisa delas,
# nao precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e nao precisam de uma explicaçao
# sobre o porque)."
# — Tim Peters (CPython Core Developer)

# object acima
# class Foo:
#     ...


Foo = type('Foo', (object,), {})
f = Foo()
# print(isinstance(f, Foo))
print(type(f))
print(type(Foo))