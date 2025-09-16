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

print('=-=' * 30)
print(f'Você digitou os valores {listas}')
