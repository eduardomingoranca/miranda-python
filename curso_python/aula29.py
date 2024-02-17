"""
Introducao ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar o numero que voce digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} eh {numero_float * 2:.2f}')
except:
    print('Isso nao eh um numero')

#if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f'O dobro de {numero_str} eh {numero_float * 2:.2f}')
#else:
#    print('Isso nao eh um numero')
