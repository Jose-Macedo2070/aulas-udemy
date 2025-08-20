# O Meu
def multiplicar(*args):
    total = 1
    for num in args:
        total *= num
    return total


# teste
print(5* 6 * 7 * 8 * 9)

print(multiplicar(5, 6, 7, 8, 9))



def verificar_par(num):
    if num % 2 == 0:
        return 'É par'
    return 'É impar'



print(verificar_par(4))