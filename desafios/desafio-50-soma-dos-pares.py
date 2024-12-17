"""
Desenvolva um programa 
que leia seis numeros inteiros
e mostre a soma apenas daqueles que forem 
pares, se o valor digitado for impar, desconsidere

"""
soma = 0
cont = 0

for contador in range(1, 7):
    num = int(input(f'Digite um numero: {contador} '))
    if num % 2 ==0:
        soma += num # Somando número
        cont += 1 # Contando número
print(f'Você informou {cont} NÚMEROS PARES, e o resultado da soma dos números são {soma}')

