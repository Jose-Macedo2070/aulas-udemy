# Introdução às funções (def) em Python
# Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
# Elas podem receber valores para parâmetros (argumentos) e retornar um valor expecífico.
# Por padrão, funções Python retornam none(nada).

# def Print(): #sintaxe
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

#Print() # Sempre que eu digitar a função igual foi passada acima ela repetirá o bloco de código detro dela 


# def imprimir(a, b, c): # a, b e c são parametros, eles são parecidos 
#     print('Várias1')   # com variáveis, e quando são definidos os  
#     print('Várias2')   # valores na função se tornam argumentos.
#     print(a, b, c)

# imprimir(1, 2, 3) # dessa forma, os valores são qualquer um,
# ...               # o intuito do "1, 2, 3" ai foi só ocupar 
# ...               # o espaço do "a, b, c"



def saudacao(nome = 'Sem nome'): #devemos pensar como se fossem 
   print(f'Olá, {nome}!')        # variáveis, logo se colocarmos um 
                                 # valor junto do "nome" que está 
                                 # acima teremos algo para ele 
                                 # printar caso a função seja  
                                 # passada vazia, isso é ultilizado 
                                 # para não quebrar o código
   

saudacao('José Macêdo')
saudacao()