primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} eh maior do que {segundo_valor=}')
elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor=} eh maior do que {primeiro_valor=}')
else:
    print(f'{primeiro_valor=} e o {segundo_valor=} sao iguais.')    
