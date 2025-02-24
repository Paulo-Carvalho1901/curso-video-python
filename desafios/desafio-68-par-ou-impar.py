"""
Faça um programa que jogue par ou impar
com o compurador. o jogo só será
interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas
que ele conquistou final do jogo
"""
from random import randint
v = 1
while True:
    jogador = int(input('Digite um valor: '))
    compurador = randint(0, 10)
    total = jogador + compurador
    tipo = ' '
    while tipo not in 'PI': 
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {compurador}. total de {total} ', end='')
    print(f'Deu par ' if total % 2 == 0 else 'Deu ímpar ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu! ')
            v += 1
        else:
            print('Você perdeu')
    print('Vamos jogar novamente!')
print(f'GAME OVER! você venceu {v} vezes')
