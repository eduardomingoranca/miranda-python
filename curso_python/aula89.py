# dir, hasattr e getattr em Python
string = 'Louis'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Nao existe o metodo', metodo)
