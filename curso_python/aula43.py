#texto = 'Python s2'

#i = 0
#tamanho_string = len(texto)

#while i < tamanho_string:
#    print(texto[i], i)

#    i += 1

#senha_salva = '123456'
#senha_digitada = ''
#repeticoes = 0

#while senha_salva != senha_digitada:
#    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#    repeticoes += 1

#print(repeticoes)
#print('Aquele laco acima pode ter repeticoes infinitas')
texto = 'Python'

nova_texto = ''
for letra in texto:
    nova_texto += f'*{letra}'
    print(letra)
print(nova_texto + '*')
