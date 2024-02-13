"""
Faca uma lista de compras com listas 
O usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua 
lista 
Nao permita que o programa quebre com
erros de indices inexistentes na lista. 
"""
loop = True
lista = []
while loop:
    option = input('Selecione uma opcao \n[i]nserir [a]pagar [l]istar: ')

    if option.casefold() != 'i' and option.casefold() != 'l'and option.casefold() != 'a':
        loop = False
        print('FIM !!!')
    else:
        if option.casefold() == 'i':
            value = input('Valor: ')
            lista.append(value)             
        elif option.casefold() == 'l':
            if len(lista) == 0:
                print(lista)
            else:    
                for indice, nome in enumerate(lista):
                    print(indice, nome)
        elif option.casefold() == 'a':
            if len(lista) == 0:
                print('A lista esta vazia.')
            else:
                delete = input('Escolha o indice para apagar: ')
                try:
                    indice = int(delete)
                    del lista[indice]
                except:
                    print('Nao foi possivel excluir este indice.')    
