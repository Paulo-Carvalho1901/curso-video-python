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