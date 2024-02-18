"""
Introducao as funcoes (def) em Python
Funcoes sao trechos de codigo usados para
replicar determinada acao ao longo do seu codigo.
Elas podem receber valores para parametros (argumentos)
e retornar um valor especifico.
Por padrao, funcoes Python retornam None (nada).
"""

# def Print():
#     print('Varias')

# Print()

# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Ola, {nome}!')

saudacao('Louis Octavius')
saudacao('Mary')    
saudacao('Helen')
saudacao()
