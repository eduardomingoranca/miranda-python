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
# __call__ da metaclass termina a execucao
#
# Metodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instancia)
#
# "Metaclasses sao magias mais profundas do que 99% dos usuarios
# deveriam se preocupar. Se voce quer saber se precisa delas,
# nao precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e nao precisam de uma explicacao
# sobre o porque)."
# — Tim Peters (CPython Core Developer)
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__ or \
                not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')

        return cls

    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')

        return instancia


class Pessoa(metaclass=Meta):
    # falar = 123

    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('MEU INIT')
        # self.nome = nome

    def falar(self):
        print('FALANDO...')


p1 = Pessoa('Louis')
p1.falar()