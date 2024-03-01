# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Voce nao passou argumentos')
else:
    try:
        print(f'Voce passou os argumentos {argumentos[1:]}')
        print(f'Faca alguma coisa com {argumentos[1]}')
        print(f'Faca outra coisa com {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')