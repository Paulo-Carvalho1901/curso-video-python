"""
Faça uma programa que leia
o peso de 5 pessoas
no final mostre qual foi o maior e o menor pesp
lidos'

"""

maiorpeso = 0
menorpeso = 0

for cont in range(1, 6):
    peso = float(input(f'Informe o peso {cont}° pessoa para analise: '))
    if cont == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'O maior peso é {maiorpeso}kg ')
print(f'O menor peso {menorpeso}kg ')
