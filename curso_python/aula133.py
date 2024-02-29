# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NAO TEM modificadores de acesso
# Mas podemos seguir as seguintes convencoes
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       nao DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguracao de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       so DEVE ser usado na classe em que foi
#       declarado.
from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso eh publico'
        self._protected = 'isso eh protegido'
        self.__exemplo = 'isso eh private'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__exemplo)
        self.__metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
# print(f.public)
print(f.metodo_publico())