"""
Escreva um programa que pergunte o salário
de um funcionario e calcule o valor do seu 
aumento

Para salários seperiores a R$1.250,00, calcule um 
aumento de 10%

para os inferiores ou iguais, o aumento é de 15%

"""

salario = float(input('Digite o valor do seu salario: '))

if salario > 1250:
    aumento1 = salario * 0.10
if salario < 1250:
   aumento1 = salario * 0.15

print(f'Seu salario com aumento é de {aumento1+salario:.2f}')

