"""
Faça um programa que leia
um número qualquer e faça seu fatorial

"""

# from math import factorial
f = 1
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
print(f'Calculando o {n}! = ', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print('x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f'{f}')
