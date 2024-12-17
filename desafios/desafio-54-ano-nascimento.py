"""
Crie um programa que leia
o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas 
ainda não atingiram a maioridade
e quantas já são maiores

"""
from datetime import date
atual = date.today().year

totalmaior = 0
totalmenor = 0

for cont in range(1, 8):
    nasc = int(input(f'Digite o {cont}° ano de nascimento: '))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Nessa contagem a {totalmaior} pessoaas maiores de idade')
print(f'E a {totalmenor} pessoas menores de idade.')