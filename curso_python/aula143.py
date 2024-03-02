# abstractmethod para qualquer metodo ja decorado (@property e setter)
# Eh possivel criar @property @property.setter @classmethod
# @staticmethod e metodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar sao palavras usadas como placeholder
# para palavras que podem mudar na programacao.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)