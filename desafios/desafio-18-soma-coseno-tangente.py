"""
Faça um programa que leia um ângulo
qualquer e mostre na tela o valor da soma,
cosseno e tangente desse ângulo

"""
from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O ânggulo de {angulo} tem o COESSENO de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} sua TANGENTE é {tangente:.2f}')






