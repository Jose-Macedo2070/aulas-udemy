
print('-' * 4, 'BEM VINDO A CALCULADORA', '-' * 4)


while True:
    num_1 = input('Digite um número inteiro: ')
    num_2 = input('Digite outro número inteiro: ')

    try:
        num_1_int = int(num_1)
        num_2_int = int(num_2)
        print('Escolha o quer fazer com os números.')
        opcao = int(input('Digite:\n[1] para somar; \n[2] para subtrair; \n[3] para multiplicar; \n[4] para dividir ou \n[0] para sair. '))
        
        if opcao == 0:
            print('Obrigado por ultilizar a nossa calculadora')
            break

        elif opcao == 1:
            print(f'Soma: {num_1_int} + {num_2_int } = {num_1_int + num_2_int}')
            continue

        elif opcao == 2:
            print(f'Subtração: {num_1_int} - {num_2_int } = {num_1_int - num_2_int}')
            continue

        elif opcao == 3:
            print(f'Multiplicação: {num_1_int} x {num_2_int } = {num_1_int * num_2_int}')
            continue

        elif opcao == 4:
            print(f'Divisão: {num_1_int} / {num_2_int } = {num_1_int / num_2_int}')
            continue
        
        else:
            print('Opção inválida, tente novamente')
        
    except:
        print('digite apenas números.')
        continue
