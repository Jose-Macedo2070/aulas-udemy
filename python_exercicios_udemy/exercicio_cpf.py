"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


# tentativa 1:
cpf = '74682489070'
#      012345678
nove_digitos = cpf[:9] #fatiamento vai do indice 0 ao 8, igual ao range aula 46 reassistir

contador_regressivo_1 = 10

resultados_digito_1 = []



for digito_1 in nove_digitos:
    conta = int(digito_1) * contador_regressivo_1
    print(f'{digito_1} x {contador_regressivo_1} =  {conta}', '\n', 10 * '-')
    resultados_digito_1.append(conta)
    contador_regressivo_1 -= 1

print(resultados_digito_1)
print( sum(resultados_digito_1) )
digito_1 = (sum(resultados_digito_1) * 10) % 11

digito_1 = digito_1 if digito_1 >= 9 else 0
print(digito_1)


    


    