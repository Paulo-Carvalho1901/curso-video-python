"""
Crie um programa que vai gera cinco números aleatórios
e coloca em uma tupla

depois disso, mostre a listagem de números
gerados também indique o maior números e o
menor valor que estão na tupla
"""

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O maior valor sorteado foi {min(numeros)}')
