"""
Melhore o jogo do desafio 28
onde o computador vai "pensar" em um 
numero entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessarios para vencer

"""

from random import randint
computador = randint(0, 10)
print('Sou seu computador acabei de pensar em um número entre 0 e 10: ')
print('Será que consegue adivinhar qual foi? ')
acertou =  False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais!')
        elif jogador > computador:
            print('Menos!')
print(f'Parabéns Acertou! voceê tentou {palpites}x')
