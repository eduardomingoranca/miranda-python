# @property - um getter no modo Pythonico
# getter - um metodo para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property eh uma propriedade do objeto, ela
# eh um metodo que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente eh usada nas seguintes situacoes:
# - como getter
# - para evitar quebrar codigo cliente
# - para habilitar setter
# - para executar acoes ao obter um atributo
# Codigo cliente - eh o codigo que usa seu codigo
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456

###########################


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)

#####################################

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta

# ###########################


# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())