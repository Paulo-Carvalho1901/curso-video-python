"""
Crie um programa onde o usuário possa
digitar sete valore númericos e cadastre-os
em uma lista unica que mantenha separados
os valores pares e ímpares. No final, mostre os valores
pares e impares em ordem crescente
"""
num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
print(f'Todos os vaLores {num}')
