import os

# Leia tambem: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# with open (context manager) e metodos uteis do TextIOWrapper
# Usamos a funcao open para abrir
# um arquivo em Python (ele pode ou nao existir)
# Modos:
# r (leitura), w (escrita), x (para criacao)
# a (escreve ao final), b (binario)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Metodos uteis
# write, read (escrever e ler)
# writelines (escrever varias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o modulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o modulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'docs/aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())


# print('#' * 10)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atencao\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.remove(caminho_arquivo) # ou unlink
# os.rename(caminho_arquivo, 'aula116-2.txt')