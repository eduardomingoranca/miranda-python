"""
Escopo de funcoes em Python
Escopo significa o local onde aquele codigo pode atingir.
Existe o escopo global e local.
O escopo global eh o escopo onde todo o codigo eh alcancavel.
O escopo local eh o escopo onde apenas nomes do mesmo local
podem ser alcancados.
"""

x = 1


def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()    
    print(x)

print(x)
escopo()
print(x)
