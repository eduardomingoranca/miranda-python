"""
Exercicio 
Peca ao usuario para digitar seu nome
Peca ao usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome eh {nome}
        Seu nome invertido eh {nome invertido}
        Se nome contem (ou nao) espacos
        Seu nome tem {n} letras
        A primeira letra do seu nome eh {letra}
        A ultima letra do seu nome eh {letra}
Se nada for digitado em nome ou idade:
    exiba 'Desculpa, voce deixou campos vazios.'
"""
nome = input('Informe o nome: ')
idade = input('Informe a idade: ')

if nome != '' and idade != '':    
    print('Seu nome eh %s' % (nome))
    print('Seu nome invertido eh %s' % (nome[::-1]))
    if ' ' in nome:
        print('O nome %s contem espaco.' % (nome))
    else:
        print('O nome %s nao contem espaco.' % (nome))    
    print('Seu nome tem %d letras' % (len(nome)))    
    print('A primeira letra do seu nome eh %s' % (nome[0]))
    print('A ultima letra do seu nome eh %s' % (nome[-1]))
else:
    print('Desculpa, voce deixou campos vazios.')
