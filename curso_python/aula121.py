# Metodos em instancias de classes Python
# Hard coded - Eh algo que foi escrito diretamente no codigo
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando...')


string = 'Louis'
print(string.upper())

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()