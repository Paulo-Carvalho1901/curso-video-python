"""
Crie um programa que leia nome e preco 
de vários produtos. O programa deverá perguntar 
se o úsuario vai continuar. 
No final mostre:

a) qual é o total gasto
b) quantos produtos custam mais de R$1000
c) qual é o nome do produto mais barato
"""
total_compra = 0
total_mil = 0
while True:
    produto = str(input('Digite o nome do produto:'))
    preco = float(input('Digite seu preço: '))
    # total da compra
    total_compra += preco
    # produtos acima de 1000
    if preco > 1000:
        total_mil += 1


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa')
print(f'O total do dos gastos foram R${total_compra} reais')
print(f'A quantidade de produto que custa mais de R$1000 reais é {total_mil}')