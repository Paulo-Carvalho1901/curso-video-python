"""
Faça uma programa que leia 5 valores
númericos e agurde-os em uma lista

no final mostre qual foi o maior
e o menor valor digitado e os seus
respectivas posições na lista

"""

listas = []

for count in range(1, 6):
    listas.append(int(input('Insira um número: ')))

print(listas)