"""
Faca um programa que peca o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva "Seu nome eh curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome eh normal"; maior que 6 escreva "Seu nome eh muito grande".
"""
nome = input('Informe o primeiro nome: ')

quantidade_letras = len(nome)
if quantidade_letras <= 4:
    print('tamanho do nome curto')
elif quantidade_letras <= 6:
    print('tamanho do nome normal')
else:
    print('tamanho do nome muito grande')
