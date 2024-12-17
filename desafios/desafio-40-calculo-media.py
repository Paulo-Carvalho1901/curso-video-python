"""
Crie um programa que leia
duas notas de um aluno e calcule sua 
media, mostrando uma mensagem no final,
de acordo com a média atingida:

Média abaixo de 5.0:
REPROVADOR

Média entre 5.0 e 6.9:
RECUPERAÇÃO

Média 7.0 ou superior:
APROVADO

"""

import datetime
import time

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2
print(f'Sua média foi {media}')
print('Aguarde seu resultado...')
time.sleep(2)

if media < 5:
    print('Aluno reprovado!')
elif media >= 5 and media <= 6.9:
    print('Aluno de recuperação')
elif media > 7:
    print('Parabéns você passou de ano!!!')