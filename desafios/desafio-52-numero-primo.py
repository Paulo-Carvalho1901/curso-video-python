"""
Faça um programa 
que leia um número inteiro
e diga se ele é ou não um número
primo
"""

num = int(input('Digite um número: '))
tot = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print(cont, end=' ')
print(f'\n\33[mO número {num} foi divisivel {tot} vezes')