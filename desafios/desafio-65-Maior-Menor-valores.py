"""
Crie um programa que leia vários
números inteiros pelo teclado
no final da execução, mostre a média entre todos
os valores e qual foi o maior e menor valores lido
o programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores

"""

resp = 'S'
soma = qtd = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = menor
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / qtd
print(f'Você digitou {num} numeros e a média foi {media:.2f}')
print(f'O maior números foi {maior} e o menos números foi {menor}')