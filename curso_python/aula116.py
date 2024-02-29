# Criando arquivos com Python + Context Manager with
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
caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
with open(caminho_arquivo, 'w') as arquivo:
    print('Ola mundo')
    print('Arquivo vai ser fechado')