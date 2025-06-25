# print(12, 34, 1011, sep="", end='\n')
# print(56, 78, sep='-', end='---------------------------')
# print(9, 10, sep='-', end='\n')





# produtos = {}

# print('----CADASTRO DE PRODUTOS----')
# while True:

#     opcao = int(input('Digite [1] para adicionar um produto ou [0] para encerrar o programa: '))


#     if opcao == 0:
#         print('Após a lista o programa será encerrado!')
#         print('Aqui estam os produtos cadastrados:')
#         for nome, valor in produtos.items():
#             print(f'O produto {nome} custa R${valor:.2f}.')
#             print('--------------------------------------')
#         break

#     elif opcao == 1:
#         nome = input('Digite o nome do produto: ')
#         valor = float(input('Digite o valor do produto: '))
#         produtos[nome] = valor
#         continue


# print(produtos[nome])


primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')



if primeiro_valor > segundo_valor:
    print(f'O valor [{primeiro_valor}] é maior que o valor [{segundo_valor}]')

elif primeiro_valor < segundo_valor:
    print(f'O valor [{segundo_valor}] é maior que o valor [{primeiro_valor}]')


