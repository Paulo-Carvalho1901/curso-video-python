"""
Escreva um programa que faça o
computadpr pensar, em um número inteiro
entre 0 e 5 e peça para usuario tentar descobrir
qual foi o número escolhido pelo computador

O programa deverá escrever na tela se úsuario venceu ou perdeu

"""
# Importando a biblioteca random
from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador PENSAR!
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # O jagador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! eu pensei no {computador} e não no {jogador}')
