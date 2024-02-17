"""
Repeticoes
while (enquanto)
Executa uma acao enquanto uma condicao for verdadeira
Loop infinito -> Quando um codigo nao tem fim
"""
quantidade_linhas = 5
quantidade_colunas = 5

linha = 1
while linha <= quantidade_linhas:
    coluna = 1
    while coluna <= quantidade_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou') 
