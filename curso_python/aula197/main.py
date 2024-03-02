# PyPDF2 para manipular arquivos PDF (PdfReader)
# PyPDF2 eh uma biblioteca de manipulacao de arquivos PDF feita em Python puro,
# gratuita e de codigo aberto. Ela eh capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotacoes, transformar paginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentacao contem todas as informacoes necessarias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdf'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20240223.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
imagem0 = page0.images[0]

# print(page0.extract_text())
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)