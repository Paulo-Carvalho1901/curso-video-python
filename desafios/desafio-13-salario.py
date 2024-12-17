"""
Faça um algoritmo que leia o salario de um 
funcionario e mostre seu novo salario, com
15% de aumento 

"""

salario = float(input('Digite seu salario R$: '))
novo_s = salario + (0.15 * salario)

print(f'Seu salario atual R${salario:.2f} seu salario com aumento de 15% é R${novo_s:.2f}')
