
# Introdução ao empacotamento e desempacotamento + tuples (tuplas)

# *resto serve para pergar o resto que não pode ser desempacotado ou por excésso de variáveis ou por excésso de valores, tambem pode ser usado "*_" tambem fica conhecido com variável.   
# se o "_" for colacado na frente ele pula os valores correspondentes da lista mas ele não coloca no resto como o "*_" ou "*resto"


# ex: Apenas com o *resto ou "*_":
nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, resto) # Maria ['Helena', 'Luiz']

# ex: com o "_":
_, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, resto)  # Helena ['Luiz']

# ex: com os dois:
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, resto)  # Luiz [] (retorna uma lista vazia por não ter valores suficientes)

