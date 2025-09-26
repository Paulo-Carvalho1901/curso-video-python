"""
Faça um programa que leia nome e peso
de varias pessoas, guardando tudo em uma lista.
No final, mostre:

a) Quantas pessoas from cadastradas
b) Uma listagem das pessoas mais pessadas
c) Uma listagem com os pessoas mais leves

"""

temp = []
princ = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    princ.append(temp[:])
    temp.clear()
    res = str(input('Quer continuar? [S/N]: '))
    if res in 'Nn':
        break
print('=-' * 30)
print(f'Os dados foram {princ}')
print(f'Ao todo você cadastrou {len(princ)} pessoas')