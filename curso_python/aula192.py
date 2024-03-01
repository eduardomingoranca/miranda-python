# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping eh o ato de "raspar a web" buscando informacoes de forma
# automatizada, com determinada linguagem de programacao, para uso posterior.
# - O modulo requests consegue carregar dados da Internet para dentro do seu
# codigo. Ja o bs4.BeautifulSoup eh responsavel por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalacao
# - pip install requests types-requests bs4
import re

import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:3333/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')

if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())