"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num = input('Digite um número inteiro: ')



# if num.isdigit():
#     num_int = int(num)

#     if num % 2 == 0:
#         print(f'O número {num_int} é par.')
    
#     elif num % 2 == 1:
#         print(f'O número {num_int} é impar.')




# else:
#     print('Digite novamente, esse número não é inteiro')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Que horas são?: ')

# try:
#     hora_int = int(hora)

#     if 0 <= hora_int <= 11:
#         print('bom dia')

#     elif 12 <= hora_int <= 17:
#         print('Boa tarde')

#     elif 18 <= hora_int <= 23:
#         print('Boa noite')

#     else:
#         print('Não conheço essa hora.')

# except:
#     print('Você não digitou um número inteiro.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""



# nome = input('Digite seu nome: ')

# if len(nome) <= 4:
#     print('Seu nome é curto')

# elif 5 <= len(nome) <= 6:
#     print('Seu nome é normal')

# elif len(nome) >= 7:
#     print('Seu nome é muito grande')