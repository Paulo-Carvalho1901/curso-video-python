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
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    res = str(input('Quer continuar? [S/N]: '))
    if res in 'Nn':
        break
print('=-' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {maior}kg.')
print(f'O menor peso foi de {menor}Kg.')