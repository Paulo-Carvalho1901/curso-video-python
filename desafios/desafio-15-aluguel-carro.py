"""
Escreva um programa que pergunte
a quantidade de km percorridos por um carro
alugado e a quantidade de dias pelos quais
ele alugado, calcule o preço a pagar, sabendo que o carro
custo R$60 por dia e
R$0,15 por km rodado

"""

qtd_dias = int(input('Digite a quantidade dias alugado: '))
km_rodado = float(input('Digite a quantidade de Km rodado: '))

dias_final = qtd_dias * 60
km_final = km_rodado * 0.15

soma = dias_final + km_final

# print(f'Digite a quantidade de dias {qtd_dias} ')
# print(f'Digite a quantidade de km rodado {km_rodado}')
print(f'Sua conta final ficou de R${soma} ')
