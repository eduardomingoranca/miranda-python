# Funcoes decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funcoes decoradoras sao funcoes que decoram outras funcoes
# Decoradores sao usados para fazer o Python
# usar as funcoes decoradoras em outras funcoes.
# Decoradores sao "Syntax Sugar" (Acúcar sintatico)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora voce foi decorada')
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123')
print(invertida)