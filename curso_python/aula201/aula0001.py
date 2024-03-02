# PySide6 para GUI (interface grafica) com Qt em Python - Instalacao
# - A secao original desse curso usou PyQt5 (estamos atualizando para PySide6)
# - Essas bibliotecas (PySide e PyQt) usam a biblioteca Qt
# - Qt eh uma biblioteca usada para a criacao de GUI (interface grafica
#   do usuario) escrita em C++.
#   - PySide e PyQt conseguem fazer a ponte (binding) entre o Python e a
#   biblioteca para a criacao de interfaces graficas sem ter que usar outra
#   linguagem de programacao.
# - PySide6 eh uma referencia a versao 6 da Qt (Qt 6)
# - Qt eh multiplataforma, ou seja, deve funcionar em Windows, Linux e Mac.

# Por que mudei de PyQt para PySide na atualizacao?
# - PySide foi desenvolvido pela The Qt Company (da Nokia), como parte do
#   projeto Qt for Python project - https://doc.qt.io/qtforpython/
# - Por usarem a mesma biblioteca (Qt), PySide e PyQt sao extremamente
#   similares, muitas vezes os codigos sao identicos. Portanto, mesmo que voce
#   ainda queira usar PyQt, sera muito simples portar os codigos. Muitas vezes
#   basta trocar o nome de PySide para PyQt e vice-versa.
# - A maior diferenca entre PyQt e PySide esta na licenca:
#   PyQt usa GPL ou commercial e PySide usa LGPL.
#   Em resumo: com PySide, voce tem a permissao uso da biblioteca para fins
#   comerciais, sem ter que compartilhar o codigo escrito por voce para o
#   publico.
#   Licencas sao topicos complexos, portanto, se oriente sobre elas
#   antes de usar qualquer software de terceiros.
#   https://tldrlegal.com/license/gnu-lesser-general-public-license-v3-(lgpl-3)
import PySide6.QtCore

# Prints PySide6 version
print(PySide6.__version__)  # type: ignore

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)  # type: ignore