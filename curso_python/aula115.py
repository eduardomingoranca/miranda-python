# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalacao
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalacao do
# ambiente virtual sera usada.
# venv eh o modulo que vamos usar para
# criar ambientes virtuais.
# Voce pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns sao:
# venv env .venv .env
#
# Como criar ambientes virtuais
# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv venv
#
# Ativando e desativando meu ambiente virtual
# Windows: .\venv\Scripts\activate
# Linux e Mac: source venv/bin/activate
# Desativar: deactivate
#
# pip - instalando pacotes e bibliotecas
# Instalar ultima versao:
# pip install nome_pacote
# Instalar versao precisa
# (tem outras formas tambem nao mencionadas)
# pip install nome_pacote==0.0.0
# Desinstalar pacote
# pip uninstall nome_pacote
# Congelar (ver pacotes)
# pip freeze
#
# Criando e usando um requirements.txt
# pip freeze > requirements.txt
# Instalando tudo do requirements.txt
# pip install -r requirements.txt