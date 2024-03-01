# __new__ e __init__ em classes Python
# __new__ eh o metodo responsavel por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ eh o metodo responsavel por inicializar
# a instancia. Por isso, init recebe self.
# __init__ ❗️NAO DEVE retornar nada (None)❗️
# object eh a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)