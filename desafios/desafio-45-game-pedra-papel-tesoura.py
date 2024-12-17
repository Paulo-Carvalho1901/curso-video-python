"""
Crei um programa que faça o
compurador jogar jokenpô com você
"""
from random import randint
import time
print('-=-'* 15)
print('JOGO JO KEN PO! TENTE SUA SORTE')
print('-=-'* 15)

item = ('PEDRA', 'PAPEL', 'TESSOURA')
computador = randint(0, 2)

print('[ 0 ] PEDRA ')
print('[ 1 ] PAPEL ')
print('[ 2 ] TESSOURA ')
jogador = int(input('Qual é sua jogada? '))
time.sleep(2)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)
print('-=-' * 15)
print(f'O computador jogou {item[computador]}')
print(f'O jogador jogou {item[jogador]}')
print('-=-' * 15)
if computador == 0: # COMPUTADOR ESCOLHEU PDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('OPÇÃO INVALIDA.')
elif computador == 1: # COMPURADOR ESCOLHEU PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('OPÇÃO INVALIDA.')
elif computador == 2: # COMPURADOR ESCOLHEU TESSOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('OPÇÃO INVALIDA.')
