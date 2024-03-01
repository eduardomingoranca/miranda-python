# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader le o CSV em formato de lista
# csv.DictReader le o CSV em formato de dicionario
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'csv/aula180.csv'

lista_clientes = [
    {'Nome': 'Louis Octavius', 'Endereco': 'Av 1, 22'},
    {'Nome': 'John Smith', 'Endereco': 'R. 2, "1"'},
    {'Nome': 'Mary Sophie', 'Endereco': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)


# lista_clientes = [
#     ['Louis Octavius', 'Av 1, 22'],
#     ['John Smith', 'R. 2, "1"'],
#     ['Mary Sophie', 'Av B, 3A'],
# ]
# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereco']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)