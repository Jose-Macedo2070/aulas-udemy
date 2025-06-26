# criar uma lista de compras com inserir, apagar e listar:
# não deixa o código quebrar com códigos inexistentes


lista_compras = []

while True:

    opcao = input('[I]- Inserir, [A]- Apagar, [L]- Listar: ').upper()
    print(40 * '-')




    if opcao == '':
        print('Você precisa digitar algo')
        print(6 * '-')
        continue

        # opcao = str(opcao.upper())


    

    if opcao == 'L':

        if lista_compras == []:
            print('Ainda não tem nada na lista.')
            continue

        print(4 * '-', 'Lista atual', 4 * '-', '\n', 40 * '-' )
       
        for produtos in lista_compras:
            print(f'{lista_compras.index(produtos)} {produtos}')
            print(6 * '-')
        
        print('Deseja sair da interação?', '\n', 40 * '-') 

        sair = input('[S]- Sair, [C]- Continuar: ').lower()
        

        if sair == 's':
            print('Obrigado pelo seu cadastro.')
            break
        
        else:
            print(40 * '-')
            continue






    elif opcao == 'I':

        produto = input('Digite o nome do produto: ')
        print(40 * '-')
        lista_compras.append(produto)
        print(f'Produto {produto} cadastrado com sucesso!!')
        print(40 * '-')
        continue
            


    elif opcao == 'A':

        if lista_compras == []:
            print('Ainda não tem nada na lista.')
            continue


        print('Aqui estão os produtos cadastrados atualmente')

        for produtos in lista_compras:
            print(f'{lista_compras.index(produtos)} | {produtos}')
            print(6 * '-')

        deletar = input('Digite o indice do produto que quer deletar: ')
        # lista_compras.remove(deletar)

        try:
            deletar_int = int(deletar)
            del(lista_compras[deletar_int])

        except:
            print('Não foi possivel deletar esse indice, tente novamente, lembrando, digite apenas números ')


        print(4 * '-', 'Lista atual', 4 * '-', '\n', 40 * '-' )

        for produtos in lista_compras:
            print(f'{lista_compras.index(produtos)} | {produtos}')
            print(6 * '-')


        continue

    else:
        print('Caracter inválido, digite algo do menu.', '\n',40 * '-')
        continue



            

