"""
Crie um programa que leia um número 
inteiro e mostre na tela se ele é PAR ou ÍMPAR

"""

num = int(input("Informe um número: "))
res = num % 2
print(f'O resultado é: {res}')

if res == 0:
    print('Número escolhido é PAR.')
else:
    print('Se Não é ÍMPAR.')