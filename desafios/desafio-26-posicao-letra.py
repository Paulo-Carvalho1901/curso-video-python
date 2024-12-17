"""
Faça um programa que leia
uma frase pelo teclado e mostre

quantas vezes a parece a letra 'A'

em que posição ela aparece a primeira vez

em que posição ela aparece a última vez

"""

frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} vezes.')
print(f'A primeira A aparece na posição {frase.find('A')}')
print(f'A última A aparece na posição {frase.rfind('A')}')