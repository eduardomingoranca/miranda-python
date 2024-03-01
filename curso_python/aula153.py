# Metodo especial __call__
# callable eh algo que pode ser executado com parenteses
# Em classes normais, __call__ faz a instancia de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'esta chamando', self.phone)
        return 2134


call1 = CallMe('23945876545')
retorno = call1('Louis Octavius')
print(retorno)
