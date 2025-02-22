"""
Crie um programa que leia varios números inteiro
pela teclado, o programa só vai parar quando o usuario digitar 999,
que é a condição da parada. No final, mostre quantos números foram digitardos
e qual foi a soma entre eles 
(desconsiderando a flag)=
"""
print('=-=' * 8, 'Leitor de números', '=-=' * 8)
soma = cont = 0
while True:
    num =  int(input('Digite um números: [999 para parar o programa]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')
