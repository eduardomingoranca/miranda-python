# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicacao
# QPushButton -> Um botao
# PySide6.QtWidgets -> Onde estao os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Texto do botao')
botao.setStyleSheet('font-size: 40px;')
botao.show()  # Adiciona o widget na hierarquia e exibe a janela

app.exec()  # O loop da aplicacao