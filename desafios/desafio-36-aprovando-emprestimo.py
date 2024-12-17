"""
Escreva um programa para aprovar empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% da
salário ou então o emprestimo será negado

"""

#Inserindo valores interação com usuário
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salario: '))
tempo = int(input('Quanto tempo deseja pagar? '))


prestacao = valor / (tempo * 12) #calculo da prestação da casa
minimo = salario * 30 / 100 # porcentagem de 30% do salario
print(f'Para pagar uma casa de R${valor} com o tempo de {tempo} anos sua prestação será de R${prestacao:.2f}')

# Condição para financiamento
if prestacao <= minimo:
    print('\33[1;32mParabéns empréstimo aprovado!\33[m ')
else:
    print('\33[1;31mDesculpe empréstimo negado!\33[m ')