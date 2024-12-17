"""
Faça um programa que leia o comprimento
de cateto aposto e do cateto adjacente de um 
triangulo retângulo, calcule e mostre o comprimento
da hipotenusa

"""
import math

oposto = float(input('Digite o seu cateto oposto: '))
adjacente = float(input('Digite o seu cateto adjacente: '))

# hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)

# print(f'A hipotenusa vai medir {hipotenusa:.2f}')

hi = math.hypot(oposto, adjacente)

print(f'A hipotenusa é {hi:.2f}')