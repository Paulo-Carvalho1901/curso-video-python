"""
Escreva um programa que leia
a valocidade de um carro

se ele ultrapassar 80km/h, mostra uma
mensagem dizendo que ele foi multado

A multa vai custar R$7,00 por cada km
acima do limite

"""

valocidade = float(input('Quala velocidade atual do seu carro? '))

if valocidade > 80:
    print('PARABÉNS! Você acaba de ser multado. Você excedeu o limite permitido que é de 80km/h')
    multa = (valocidade - 80) * 7
    print(f'Você deve ágar uma multa de R${multa:.2f}')
else:
    print('Tenha um bom dia! dirija com segurança')

