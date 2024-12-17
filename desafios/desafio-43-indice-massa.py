"""
Desenvolva uma logica que leia o peso e altura de uma 
pessoa, calcule seu IMC e mostre seu status, de acordo
com a tabela a baixo:

abaixo dse 18.5: abaixo do peso
entre 18.5 e 25: peso ideial
25 até 30: sobrepesso
30 até 40: obsidade
acima de 40:
Obsidade mórbida
"""

altura = float(input('Digite sua altura? (m)'))
peso = float(input('Digite seu peso? (kg)'))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu {peso}Kg e seu IMC é {imc:.2f} você esta abaixo do peso NORMAL! cuidado!')
elif imc >= 18.5 and imc < 25:
    print(f'Seu {peso}Kg e seu IMC é {imc:.2f} Você está com o peso IDEAL. ')
elif imc > 25 and imc < 30:
    print(f'Seu {peso}Kg e seu IMC é {imc:.2f} Vocé está com SOBREPESO fazer dieta. ')
elif imc >= 30 and imc < 40:
    print(f'Seu {peso}Kg e seu IMC é {imc:.2f} Você está com OBSIDADE CUIDADO! ')
elif imc > 40:
    print(f'Seu {peso}Kg e seu IMC  é {imc:.2f} Você está com OBSIDADE MORBIDA, procurar ajuda de um expecialista URGENTE! ')