"""
Calculo do primeiro digito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva comecando de 10

Ex.: 746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisao da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado eh 0
contrario disso:
    resultado eh o valor da conta

O primeiro digito do CPF eh 7        
"""
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo = 10
soma_digitos = 0

for digito in nove_digitos:
    soma_digitos = soma_digitos + (int(digito) *  contador_regressivo)
    contador_regressivo = contador_regressivo - 1

mod = soma_digitos * 10 % 11

validacao_cpf = 'CPF valido!' if mod == int(cpf[:1]) else 'CPF invalido!'
print(validacao_cpf)
