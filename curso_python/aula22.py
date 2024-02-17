# Operadores logicos
# and (e) or (ou) not (nao)
# and - Todas as condicoes precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressao inteira sera avaliada naquele valor
# Sao considerados falso 
# 0.0.0 '' False
# Tambem existe o tipo None que eh
# usado para representar um nao valor

#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')

#senha_permitida = '123456'

#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#    print('Entrar')
#else:
#    print('Sair') 

# Avaliacao de curto circuito
print(True or False or 0)
print(0 or False or 0 or 'abc' or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)
