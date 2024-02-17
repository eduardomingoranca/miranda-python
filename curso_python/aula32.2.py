"""
Faca um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudacao apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Informe o horario: ')


try:
    horario_integer = int(horario) 
    if horario_integer >= 0 and horario_integer <= 11:
        print('Bom dia')
    elif horario_integer >= 12 and horario_integer <= 17:
        print('Boa tarde')
    elif horario_integer >= 18 and horario_integer <= 23:
        print('Boa noite')    
except:    
    print('valor %s invalido.' % (horario))
