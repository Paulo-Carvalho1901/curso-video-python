"""
Desenvolva um programa que leia o 
primeiro termo e a razão de uma PA, 
no final, mostre os 10 primeiros termos
dessa progressão
"""
print('Progressão aritmetica PA')
print()
primeiro_termo = int(input('Primeiro termo '))
razao = int(input('Razão. '))
decimo = primeiro_termo + (10 - 1) * razao

for cont in range(primeiro_termo, decimo + razao, razao):
    print(cont, end=' -> ')
print('ACABOU')

#Contagem de traz para frente
# for cont in range(10, -1, -1):
#     print(cont)