lista = [ 'luiz', 'claudia', 'maria' ]


# for nomes in lista:

#     print(f'{lista.index(nomes)}, {nomes}')

# existe um jeito mais fácil de fazer isso :

# lista_enumerada = enumerate(lista) dessa forma aparece o iterator e não a lista em si, para que apareça a lista, precisamos do for ou do next mas depois disso o enumerate que gera um interator que  "consome" a lista fazendo com que reste apenas o iterator e mais nenhum valor.

# print(next(lista_enumerada))
# for item in lista_enumerada:
#     print(item)

# Após aqui não é printado mais nada.

# for item in lista_enumerada:
#     print(item)



# lista_enumerada = lista
# print(lista_enumerada)

    # porem se a váriavel lista_enumerada = enumerate(lista) não existir e se jogarmos o valor dela direto em um for o interator não consome os valores.
    
    # ex: usando várias vezes para verificar se é permitido 

# for item in enumerate(lista):
#     print(item)
# for item in enumerate(lista):
#     print(item)
# for item in enumerate(lista):
#     print(item)
# for item in enumerate(lista):
#     print(item)