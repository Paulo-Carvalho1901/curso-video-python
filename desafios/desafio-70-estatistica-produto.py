"""
Crie um programa que leia nome e preco 
de vários produtos. O programa deverá perguntar 
se o úsuario vai continuar. 
No final mostre:

a) qual é o total gasto
b) quantos produtos custam mais de R$1000
c) qual é o nome do produto mais barato
"""
while True:
    produto = str(input('Digite o nome do produto:'))
    preco = float(input('Digite seu preço: '))

    


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print('Fim do programa')