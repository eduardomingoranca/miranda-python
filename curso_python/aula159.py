# dataclasses - O que sao dataclasses?
# O módulo dataclasses fornece um decorador e funcoes para criar metodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuario.
# Em resumo: dataclasses sao syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versao 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


if __name__ == '__main__':
    p1 = Pessoa('Louis', 30)
    p2 = Pessoa('Louis', 30)
    print(p1 == p2)