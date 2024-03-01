# Exercicio - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instancias
# da classe com os dados salvos
# Faca em arquivos separados.
import json

CAMINHO_ARQUIVO = 'json/aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('John', 33)
p2 = Pessoa('Helen', 21)
p3 = Pessoa('Jennifer', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('ELE EH O __main__')
    fazer_dump()