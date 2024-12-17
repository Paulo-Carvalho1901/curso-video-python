"""
Desenvolva um programa que pergunte a distância
de uma viagem em km, calcule o preço da passagem cobrando
R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas

"""

distancia = float(input('Digite a distancia total da viagem: '))
print(f'Sua viagem esta pra começar uma viagem de {distancia} km')

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco =  distancia * 0.45
print(f'O valor a ser pago da sua viagem será: R${preco}')