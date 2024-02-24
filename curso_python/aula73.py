"""
Higher Order Functions
Funcoes de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)


print(executa(saudacao, 'Bom dia', 'Louis'))
print(executa(saudacao, 'Bom noite', 'Mary'))

