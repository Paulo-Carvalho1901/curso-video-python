"""
A confederação nascional de notação
precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria
de acordo com sua idade

atá 9 anos: mirim
até 14 anos: infantil
até 19 anos: junior
até 20 anos: sênior
Acima: mestre

"""

from datetime import date

ano_nascimento = int(input('Digite seu ano de nascimento: '))
atual = date.today().year # capiturando o ano atual
idade = atual - ano_nascimento
print(f'O atleta tem {idade} anos: ')

if idade <= 9:
    print('Atleta é MIRIM')
elif idade <= 14:
    print('Atleta é INFANTIL')
elif idade <= 19:
    print('Atleta é JUNIOR')
elif idade <= 25:
    print('Atleta é SÊNIOR')
else:
    print('Atleta é MASTER')
