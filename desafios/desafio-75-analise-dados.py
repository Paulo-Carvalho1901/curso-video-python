"""
Crie um programa que leia 
quatro valores pelo teclado
e os guarde-os em uma tupla
no final mostre

a) Quantas vazes apareceu o numeros 9
b) Em que posição foi digitado o primeiro 
valor 3
c) Quais foram os numeros pares
"""

num = (int(input('Digite o número 1: ')),
       int(input('Digite o número 2: ')),
       int(input('Digite o número 3: ')),
       int(input('Digite o número 4: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apreceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apreceu na {num.index(3)+1}° posição.')
else:
    print('O valor 2  não foi encontrado em nenhum posição.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
