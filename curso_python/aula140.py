# Heranca Multipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# varias outras classes.
# Heranca simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Heranca multipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# metodo -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (eh complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos metodos
# Use o metodo de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)