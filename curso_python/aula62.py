"""
Calculo do segundo digito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva comecando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77  40 54 64 14 24 40 36 0  14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisao da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado eh 0
contrario disso:
    resultado eh o valor da conta    

O segundo digito do CPF eh 0    
"""
cpf = '7468248907'
dez_digitos = cpf[:10]
contador_regressivo = 11
soma_digitos = 0

for digito in dez_digitos:
    soma_digitos = soma_digitos + (int(digito) * contador_regressivo)
    contador_regressivo = contador_regressivo - 1

mod = soma_digitos * 10 % 11    

validacao_cpf = 'CPF valido!' if mod == int(cpf[8]) else 'CPF invalido!'
print(validacao_cpf)
