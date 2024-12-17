"""
Crie um programa que leia quanto
dinheiro uma pessoa tem na carteira
e mostre quantos dólares éla pode comprar

"""

valor = float(input('Digite seu valor na carteira R$: '))
dolar = valor / 5.78

print(f'Com esse você pode comprar {dolar:.2f} dólares.')
