"""
Crie um programa que leia varios números
inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição
que parada. No final, mostre quantos números foram
digitados e qual foi o soma entre eles
desconsiderandoa flag
"""
numero = cont = soma = 0
numero = int(input('Digite número 999 para parar! '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite número 999 para parar! '))
print(f'Você digitou {cont} números e a soma entre eles é {soma} ')