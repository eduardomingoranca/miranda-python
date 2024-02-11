frase = 'O Python eh uma linguagem de programacao ' \
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum'

#frase = 'oooaaa'
#print(frase.upper())
#print(frase.lower())
#print(frase.count('Python'))
#print(frase.count('o'))

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)