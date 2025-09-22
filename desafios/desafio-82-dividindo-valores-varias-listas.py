"""
Crie um programa que vai ter vários números
e colocar em uma lista

Depois disso, crie duas listas extras que vão
contar apenas os valores pares e os valores impares
digitados, respectivamente

Ao final, mostre o conteúdo das três listas grandes.

"""

lista_mae = []
lista_par = []
lista_impar = []

while True:
    lista_mae.append(int(input('Digite um valor: ')))
    res = str(input('Gostaria de continuar? [S/N]: '))
    if res in 'Nn':
        break

print(f'Minha lista completa é {lista_mae}')
