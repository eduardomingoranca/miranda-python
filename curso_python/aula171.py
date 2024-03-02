# os.walk para navegar de caminhos de forma recursiva
# os.walk eh uma funcao que permite percorrer uma estrutura de diretorios de
# maneira recursiva. Ela gera uma sequencia de tuplas, onde cada tupla possui
# tres elementos: o diretorio atual (root), uma lista de subdiretorios (dirs)
# e uma lista dos arquivos do diretorio atual (files).
import os
from itertools import count

caminho = os.path.join('/Users', 'eduar', 'Workspace', 'EXEMPLO')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
        # NAO FACA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)
        