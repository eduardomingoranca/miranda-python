"""
Faca um jogo para o usuario adivinhar qual a palavra secreta.
- Voce vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuario digitar apenas uma letra.
- Qual o usuario digitar uma letra, voce vai conferir se a letra 
digitada esta na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada nao estiver na palavra secreta; exiba *.
Faca a contagem de tentativas do seu usuario.    
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas = numero_tentativas + 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas = letras_acertadas + letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada = palavra_formada + letra_secreta
        else:
            palavra_formada = palavra_formada + '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABENS!')
        print('A palavra era %s' % (palavra_secreta))
        print('Tentativas: %d' % (numero_tentativas))
        letras_acertadas = ''
        numero_tentativas = 0
