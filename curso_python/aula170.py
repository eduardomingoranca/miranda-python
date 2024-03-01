# os.listdir para navegar em caminhos
# /Users/eduar/Workspace/EXEMPLO
# C:\Users\eduar\Workspace\EXEMPLO
# caminho = r'C:\\Users\\eduar\\Workspace\\EXEMPLO'
import os

caminho = os.path.join('\Users', 'eduar', 'Workspace', 'EXEMPLO')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)
