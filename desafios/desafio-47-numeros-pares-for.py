"""
Crie um programa que mostre
na tela todos os numeros
pares que estão no intervalo entre 1 e 50

"""

for cont in range(2, 51, 2):
    print(cont, end=' ')
print('Acabou! ') 

for num in range(1, 51):
    if num % 2 == 0: # TESTANDO SE UM NUMERO É DIVISIVEL POR 2
        print(num, end=' ')
print('Acabou! ')