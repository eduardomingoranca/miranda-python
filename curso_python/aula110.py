# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Louis', 'nota': 'A'},
    {'nome': 'Lauren', 'nota': 'B'},
    {'nome': 'Felicity', 'nota': 'A'},
    {'nome': 'Rose', 'nota': 'C'},
    {'nome': 'Jennifer', 'nota': 'D'},
    {'nome': 'John', 'nota': 'A'},
    {'nome': 'Edward', 'nota': 'B'},
    {'nome': 'Andrew', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
        