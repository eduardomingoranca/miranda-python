# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Voce pode implementar seus proprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso eh chamado de Duck typing. Um conceito
# relacionado com tipagem dinamica onde o Python nao
# esta interessado no tipo, mas se alguns metodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um passaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele passaro de pato.
# Para criar um context manager, os metodos __enter__ e __exit__
# devem ser implementados.
# O metodo __exit__ recebera a classe de excecao, a excecao e o
# traceback. Se ele retornar True, excecao no with sera
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...
class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()


with MyOpen('docs/aula149.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)