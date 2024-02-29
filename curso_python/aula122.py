# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instancia da class (objeto) - Tem os dados
# Uma classe pode gerar varias instancias.
# Na classe o self eh a propria instancia.
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando...')


fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
celta.acelerar()
Carro.acelerar(celta)
# print(celta.nome)