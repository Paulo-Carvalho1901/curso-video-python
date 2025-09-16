"""
Faça uma programa que leia 5 valores
númericos e agurde-os em uma lista

no final mostre qual foi o maior
e o menor valor digitado e os seus
respectivas posições na lista

"""

listas = [] 

# criando variaveis para armazenar maiores e menores valores
maior = 0
menor = 0

for count in range(0, 5):
    listas.append(int(input(f'Digite um valor para a posiççao {count}: ')))
    # criado condição para verificar maior e menor valor
    if count == 0:
        maior = menor = listas[count]
    else:
        if listas[count] > maior:
            maior = listas[count]
        if listas[count] < menor:
            menor = listas[count]
print('=-=' * 30)
print(f'Você digitou os valores {listas}')
print(f'O meior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(listas):
    if valor == maior:
        print(f'{indice}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(listas):
    if valor == menor:
        print(f'{indice}... ', end='')
